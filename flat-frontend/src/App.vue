<script setup lang="ts">
  import { RouterLink } from "vue-router";
  // This starter template is using Vue 3 <script setup> SFCs
  // Check out https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup
</script>

<template>
  <nav
    class="lg:fixed lg:mt-4 lg:mr-4 lg:right-0 lg:w-auto lg:ml-4 sticky top-0 w-full :justify-center items-center"
  >
    <ul
      class="flex gap-4 justify-center lg:flex-col rounded bg-black p-4 shadow-xl"
    >
      <li>
        <RouterLink
          class="text-sm text-white font-semibold bg-black underline decoration-transparent hover:decoration-inherit transition duration-300 ease-in-out active:text-gray-800"
          to="/"
        >
          Home</RouterLink
        >
      </li>
      <li>
        <RouterLink
          to="/pull-request"
          class="text-sm text-white font-semibold bg-black underline decoration-transparent hover:decoration-inherit transition duration-300 ease-in-out active:text-gray-500"
        >
          Pull Request</RouterLink
        >
      </li>
      <li>
        <RouterLink
          to="/new-pull-request"
          class="text-sm text-white font-semibold bg-black underline decoration-transparent hover:decoration-inherit transition duration-300 ease-in-out active:text-gray-800"
        >
          Crear PR</RouterLink
        >
      </li>
    </ul>
  </nav>
  <div class="flex flex-col flex-grow p-4 pt-8">
    <router-view></router-view>
  </div>
</template>
