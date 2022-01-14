<script setup lang="ts">
  import { ref, onMounted, Ref } from "vue";
  import { useRoute, RouterLink } from "vue-router";
  import { getCommitDetail, Commit } from "@/data/axiosConfig";
  const commitData: Ref<Commit | undefined> = ref();
  const route = useRoute();
  onMounted(async function () {
    const response = await getCommitDetail(route.params.id as string);
    commitData.value = response.data;
  });
</script>
<template>
  <div v-if="commitData" class="flex flex-grow flex-col items-center">
    <h1 class="font-bold text-xl">Detalle de commit {{ route.params.id }}</h1>
    <ul class="my-4">
      <li class="my-2">
        <p class="text-xs text-gray-600 font-bold mt-2 flex flex-col">
          <span>
            Author:
            {{ commitData.author.name }}
          </span>
          <span>
            Email:
            {{ commitData.author.email }}
          </span>
        </p>
      </li>
      <li class="my-2">
        <p class="text-xs text-gray-600 font-bold mt-2 flex flex-col gap-3">
          <span class="text-base">Total</span>
          <span>
            Delations:
            {{ commitData.total_stats.deletions }}
          </span>
          <span>
            Insertions:
            {{ commitData.total_stats.insertions }}
          </span>
          <span>
            Files:
            {{ commitData.total_stats.files }}
          </span>
          <span>
            Lines:
            {{ commitData.total_stats.lines }}
          </span>
        </p>
      </li>
      <li class="my-2">
        <p class="text-xs text-gray-600 font-bold mt-2">
          Fecha: {{ new Date(commitData.datetime).toLocaleDateString("es-MX") }}
          {{ new Date(commitData.datetime).toLocaleTimeString("es-MX") }}
        </p>
      </li>
    </ul>
    <ul
      v-if="commitData.files_stats.length > 0"
      class="mt-8 w-full px-4 pb-8 overflow-hidden"
    >
      <li
        class="mt-4 w-full"
        v-for="file in commitData.files_stats"
        :key="file.file_name"
      >
        <div class="flex justify-center">
          <div class="block p-6 rounded-lg shadow-lg bg-white w-full max-w-lg">
            <h5
              class="text-gray-900 text-xl leading-tight font-medium mb-2 truncate"
            >
              {{ file.file_name }}
            </h5>

            <p
              class="text-gray-600 font-bold text-base mb-4 flex flex-col gap-3"
            >
              <span class="text-sm truncate">File: {{ file.file_name }} </span>
              <span>Delations: {{ file.deletions }} </span>
              <span>Insertions: {{ file.insertions }} </span>
              <span>Lines: {{ file.lines }} </span>
            </p>
          </div>
        </div>
      </li>
    </ul>
  </div>
</template>
