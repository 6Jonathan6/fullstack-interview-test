const routes = [
  {
    name: "home",
    path: "/",
    component: () => import("@/components/Home.vue"),
  },
  {
    name: "branch-detail",
    path: "/branches/:id",
    component: () => import("@/components/BranchDetail.vue"),
  },
  {
    name: "commit-detail",
    path: "/commit/:id",
    component: () => import("@/components/CommitDetail.vue"),
  },
];
export default routes;
