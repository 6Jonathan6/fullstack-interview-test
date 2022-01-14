<script setup lang="ts">
  import ErrorModal from "@/components/ErrorModal.vue";
  import { ref, onMounted, Ref } from "vue";
  import { useRouter } from "vue-router";
  import {
    getBranches,
    PULL_REQUEST_STATUSES,
    PR_STATUS_LABELS,
    createPullRequest,
  } from "@/data/axiosConfig";

  const branches: Ref<string[]> = ref([]);
  const loading = ref(false);
  const compareBranch = ref("");
  const baseBranch = ref("");
  const errorMessage: Ref<string> = ref("");
  const router = useRouter();

  onMounted(async function () {
    const result = await getBranches();
    branches.value = result.data;
  });
  async function onSubmit(event: Event) {
    try {
      loading.value = true;
      const formData = new FormData(event.currentTarget as HTMLFormElement);
      const fieldValues = Object.fromEntries(formData.entries());
      const createPrPayload = {
        status: fieldValues.status,
        base_branch_name: fieldValues["base-branch"],
        compare_branch_name: fieldValues["compare-branch"],
        merge_commit_message: fieldValues.description,
        pr_title: fieldValues.title,
        author: fieldValues.author,
      };
      await createPullRequest(createPrPayload);
      router.push({ name: "pull-request-list" });
    } catch (error: any) {
      if (error.isAxiosError) {
        const isReponseArray = Array.isArray(error.response.data);
        errorMessage.value = isReponseArray
          ? `Code: ${error.response.status} ${error.response.data[0]}`
          : error.message;
      } else {
        errorMessage.value = error.message;
      }
    } finally {
      loading.value = false;
    }
  }
  function onError(error: string) {
    errorMessage.value = error;
  }
</script>
<template>
  <div class="flex flex-grow flex-col items-center">
    <h1 class="font-bold text-xl">Crear pull-request</h1>
    <form
      class="flex flex-col max-w-3xl w-full mt-8 p-4 shadow-md rounded"
      @submit.prevent="onSubmit"
    >
      <p v-if="baseBranch && compareBranch" class="text-xl my-4">
        Merge <span class="font-bold">{{ compareBranch }}</span> into
        <span class="font-bold">{{ baseBranch }}</span>
      </p>
      <fieldset class="border rounded">
        <div class="p-4">
          <label for="status" class="mr-4">Estatus</label>
          <select
            id="status"
            required
            name="status"
            class="border rounded border-gray-300 py-2"
          >
            <option
              v-for="option in PULL_REQUEST_STATUSES"
              :value="option"
              :key="option"
            >
              {{ PR_STATUS_LABELS[option] }}
            </option>
          </select>
        </div>
        <div class="p-4">
          <label for="compare-branch" class="mr-2">Compare branch:</label>
          <input
            v-model="compareBranch"
            id="compare-branch"
            list="branches"
            name="compare-branch"
            required
            class="border-b border-black"
          />
          <datalist id="branches">
            <option v-for="branch in branches" :value="branch"></option>
          </datalist>
        </div>
        <div class="p-4">
          <label for="base-branch" class="mr-2">Base branch:</label>
          <input
            v-model="baseBranch"
            id="base-branch"
            list="branches"
            name="base-branch"
            required
            class="border-b border-black"
          />
          <datalist id="branches">
            <option v-for="branch in branches" :value="branch"></option>
          </datalist>
        </div>
      </fieldset>
      <fieldset class="border rounded p-4 flex justify-between mt-2">
        <ul class="flex flex-col gap-4 w-full">
          <li>
            <label for="title" class="mr-2">Título</label>
            <input
              id="title"
              class="border-b border-black w-full"
              required
              name="title"
            />
          </li>
          <li class="flex flex-col">
            <label for="description" class="mr-2">Descripción</label>
            <textarea
              id="description"
              class="border border-gray-300 w-full p-2"
              name="description"
              required
              rows="10"
            />
          </li>
        </ul>
      </fieldset>
      <fieldset class="border rounded p-4 mt-2">
        <label for="Author" class="mr-2">Autor</label>
        <input
          id="Author"
          class="border-b border-black w-full"
          required
          name="author"
        />
      </fieldset>
      <fieldset class="flex w-full justify-end items-center">
        <button
          type="submit"
          :disabled="loading"
          class="inline-block mt-8 ml-auto px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
        >
          GUARDAR
        </button>
      </fieldset>
    </form>
  </div>
  <ErrorModal
    v-if="errorMessage"
    :messege="errorMessage"
    @close="errorMessage = ''"
  />
</template>
