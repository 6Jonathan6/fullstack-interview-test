<script setup lang="ts">
  import { ref, onMounted, Ref } from "vue";
  import { useRoute, RouterLink } from "vue-router";
  import { getBranchDetail, Commit } from "@/data/axiosConfig";
  const branchData: Ref<Commit[]> = ref([]);
  const route = useRoute();
  onMounted(async function () {
    const response = await getBranchDetail(route.params.id as string);
    branchData.value = response.data;
  });
</script>
<template>
  <div class="flex flex-grow flex-col items-center">
    <h1 class="font-bold text-xl">Detalle de: {{ route.params.id }}</h1>
    <ul v-if="branchData.length > 0">
      <li class="mt-4" v-for="commit in branchData" :key="commit.id">
        <div class="flex justify-center">
          <div class="block p-6 rounded-lg shadow-lg bg-white w-full max-w-sm">
            <h5 class="text-gray-900 text-xl leading-tight font-medium mb-2">
              {{ commit.short_sha }}
            </h5>
            <p class="text-gray-700 text-base mb-4">
              {{ commit.message }}
            </p>
            <p class="text-gray-600 font-bold text-base mb-4">
              Autor: {{ commit.author.name }} <br />
              Email: {{ commit.author.email }}
            </p>
            <RouterLink
              :to="{ name: 'commit-detail', params: { id: commit.short_sha } }"
              class="inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
            >
              Ver detalle
            </RouterLink>
            <p class="text-xs text-gray-600 font-bold mt-2 text-right">
              {{ new Date(commit.datetime).toLocaleDateString("es-MX") }}:
              {{ new Date(commit.datetime).toLocaleTimeString("es-MX") }}
            </p>
          </div>
        </div>
      </li>
    </ul>
  </div>
</template>
