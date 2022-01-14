<script setup lang="ts">
  import { computed, Ref, ref, defineEmits } from "vue";
  import {
    PR_STATUSES_UNION,
    PR_STATUS_LABELS,
    PULL_REQUEST_STATUS_OPEN,
    PULL_REQUEST_STATUS_MERGED,
    PULL_REQUEST_STATUS_CLOSED,
    updatePullRequest,
    PullRequest,
  } from "@/data/axiosConfig";

  interface Props {
    id: number;
    status: PR_STATUSES_UNION;
    base_branch_name: string;
    compare_branch_name: string;
    created_at: string;
    updated_at: string;
    merge_commit_message: string;
    pr_title: string;
    author: string;
  }
  const props = defineProps<Props>();
  const emit = defineEmits(["error", "updated"]);
  const statusLabel = computed(() => PR_STATUS_LABELS[props.status]);
  const loading = ref(false);
  const mergedStatus: Ref<typeof PULL_REQUEST_STATUS_MERGED> = ref(
    PULL_REQUEST_STATUS_MERGED
  );
  const closedStatus: Ref<typeof PULL_REQUEST_STATUS_CLOSED> = ref(
    PULL_REQUEST_STATUS_CLOSED
  );

  async function onClick(id: number, status: PR_STATUSES_UNION) {
    try {
      loading.value = true;
      const response = await updatePullRequest(id, status);
      emit("updated", response.data);
    } catch (error: any) {
      if (error.isAxiosError) {
        const isReponseArray = Array.isArray(error.response.data);
        emit(
          "error",
          isReponseArray
            ? `Code: ${error.response.status} ${error.response.data[0]}`
            : error.message
        );
      } else {
        emit("error", error.message);
      }
    } finally {
      loading.value = false;
    }
  }
</script>
<template>
  <li class="mt-4 w-full">
    <div class="flex justify-center">
      <div class="block p-6 rounded-lg shadow-lg bg-white w-full max-w-lg px-4">
        <div class="w-full flex justify-end">
          <p
            :class="{
              'bg-red-900': props.status === PULL_REQUEST_STATUS_CLOSED,
              'bg-blue-800': props.status === PULL_REQUEST_STATUS_MERGED,
              'bg-gray-700': props.status === PULL_REQUEST_STATUS_OPEN,
            }"
            class="py-1 px-2 rounded text-white font-bold shadow-inner"
          >
            {{ statusLabel }}
          </p>
        </div>
        <h5 class="text-gray-900 text-xl leading-tight font-bold mb-2 truncate">
          {{ props.pr_title }}
        </h5>
        <p class="text-gray-700 text-base mb-4">
          {{ props.merge_commit_message }}
        </p>
        <p class="text-gray-700 text-base mb-4">
          Merge
          <span class="font-bold"> {{ props.compare_branch_name }}</span> into
          <span class="font-bold">{{ props.compare_branch_name }} </span>
        </p>
        <div class="flex flex-col">
          <ul class="mt-4">
            <li>
              <p class="text-xs text-gray-600 font-bold mt-2 text-right">
                Author: {{ props.author }}
              </p>
            </li>
            <li>
              <p class="text-xs text-gray-600 font-bold mt-2 text-right">
                Creado:
                {{ new Date(props.created_at).toLocaleDateString("es-MX") }}
                {{ new Date(props.created_at).toLocaleTimeString("es-MX") }}
              </p>
            </li>
            <li>
              <p class="text-xs text-gray-600 font-bold mt-2 text-right">
                Actualizado:
                {{ new Date(props.updated_at).toLocaleDateString("es-MX") }}
                {{ new Date(props.updated_at).toLocaleTimeString("es-MX") }}
              </p>
            </li>
          </ul>
          <div class="flex w-full items-center justify-end mt-6">
            <button
              v-if="props.status === PULL_REQUEST_STATUS_OPEN"
              @click="onClick(props.id, closedStatus)"
              :disabled="loading"
              :class="{ 'bg-gray-400': loading, 'bg-red-900': !loading }"
              class="inline-block ml-auto px-6 py-2.5 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-red-700 hover:shadow-lg focus:bg-red-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-red-800 active:shadow-lg transition duration-150 ease-in-out"
            >
              CLOSE
            </button>
            <button
              v-if="props.status === PULL_REQUEST_STATUS_OPEN"
              @click="onClick(props.id, mergedStatus)"
              :disabled="loading"
              :class="{ 'bg-gray-400': loading, 'bg-blue-800': !loading }"
              class="inline-block ml-4 px-6 py-2.5 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
            >
              MERGE
            </button>
          </div>
        </div>
      </div>
    </div>
  </li>
</template>
