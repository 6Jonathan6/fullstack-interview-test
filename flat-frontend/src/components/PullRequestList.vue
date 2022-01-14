<script setup lang="ts">
  import { ref, onMounted, Ref } from "vue";
  import { getPullRequests, PullRequest } from "@/data/axiosConfig";
  import PullRequestCardVue from "@/components/PullRequestCard.vue";
  const pullRequests: Ref<PullRequest[]> = ref([]);
  onMounted(async function () {
    const response = await getPullRequests();
    pullRequests.value = response.data.reverse();
  });
  function onUpdated(updatedPr: PullRequest) {
    pullRequests.value = pullRequests.value.map((pr) => {
      if (pr.id === updatedPr.id) {
        return updatedPr;
      }
      return pr;
    });
  }
</script>
<template>
  <div class="flex flex-grow flex-col items-center">
    <h1 class="font-bold text-xl">Pull Requests List</h1>
    <ul class="mt-8 w-full px-4 pb-8 overflow-hidden">
      <PullRequestCardVue
        v-for="pr in pullRequests"
        :author="pr.author"
        :base_branch_name="pr.base_branch_name"
        :compare_branch_name="pr.compare_branch_name"
        :created_at="pr.created_at"
        :merge_commit_message="pr.merge_commit_message"
        :pr_title="pr.pr_title"
        :status="pr.status"
        :id="pr.id"
        :updated_at="pr.updated_at"
        :key="pr.id"
        @updated="onUpdated"
      />
    </ul>
  </div>
</template>
