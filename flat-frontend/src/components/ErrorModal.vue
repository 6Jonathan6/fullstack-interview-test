<script setup lang="ts">
  const props = defineProps<{
    messege: string;
  }>();
  const emit = defineEmits(["close"]);
</script>
<template>
  <div
    class="modal fade fixed top-0 left-0 right-0 lg:mt-8 mx-auto w-full h-full outline-none overflow-x-hidden overflow-y-auto max-w-screen-md"
    id="exampleModal"
    tabindex="-1"
    aria-labelledby="exampleModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog relative w-auto pointer-events-none text-white">
      <div
        class="modal-content border-none shadow-lg relative flex flex-col w-full pointer-events-auto bg-red-900 text-white bg-clip-padding rounded-md outline-none text-current"
      >
        <div
          class="modal-header flex flex-shrink-0 items-center justify-between p-4 border-b border-gray-200 rounded-t-md"
        >
          <h5
            class="text-xl font-medium leading-normal text-white"
            id="exampleModalLabel"
          >
            Error
          </h5>
          <button
            @click="$emit('close')"
            type="button"
            class="btn-close box-content bg-slate-500 flex items-center justify-center w-4 h-4 p-1 text-white border-none rounded-none opacity-50 focus:shadow-none focus:outline-none focus:opacity-100 hover:text-white hover:opacity-75 hover:no-underline"
            aria-label="Close"
          >
            X
          </button>
        </div>
        <div class="modal-body relative p-4">{{ props.messege }}</div>
      </div>
    </div>
  </div>
</template>
