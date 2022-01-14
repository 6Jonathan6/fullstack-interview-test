<script setup lang="ts">
  import { getBranches } from "@/data/axiosConfig";
  import { onMounted, ref, Ref } from "vue";
  import { RouterLink } from "vue-router";

  const branches: Ref<string[]> = ref([]);
  onMounted(async function () {
    const result = await getBranches();
    branches.value = result.data;
    console.log(branches.value);
  });
</script>

<template>
  <div class="flex flex-grow flex-col items-center">
    <h1 class="font-bold text-xl">Branches</h1>
    <ul>
      <li class="mt-4" v-for="branch in branches" :key="branch">
        <div class="flex justify-center">
          <div
            class="flex flex-col p-6 rounded-lg shadow-lg bg-white w-full lg:max-w-sm"
          >
            <h5 class="text-gray-900 text-xl leading-tight font-medium mb-4">
              {{ branch }}
            </h5>
            <RouterLink
              :to="{ name: 'branch-detail', params: { id: branch } }"
              class="inline-block ml-auto px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
            >
              Ver detalle
            </RouterLink>
          </div>
        </div>
      </li>
    </ul>
  </div>
</template>
