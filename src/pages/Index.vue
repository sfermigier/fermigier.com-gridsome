<template>
  <Layout>
    <div
      class="hero container-inner mx-auto flex flex-col sm:flex-row justify-between py-16"
    >
      <div class="text-4xl font-bold w-full sm:w-3/5 text-center sm:text-left">
        <div class="leading-tight">Stefane Fermigier</div>
        <div class="text-brand-700 leading-tight">Fullstack entrepreneur</div>
      </div>

<!--      <div class="mt-8 sm:mt-0">-->
<!--        <g-image-->
<!--          src="../../static/developer.svg"-->
<!--          alt="hero"-->
<!--          class="mx-auto sm:mx-0"-->
<!--        />-->
<!--      </div>-->
    </div>
    <!-- end hero -->

    <div class="container-inner mx-auto mb-16 content text-xl sm:text-xl">
      <div v-html="$page.block.content"></div>
    </div>
  </Layout>
</template>

<page-query>
query Block {
  block (path: "/blocks/home-about") {
    title
    content
  }
}
</page-query>


<script>
export default {
  metaInfo: {
    title: "Home",
  },
};
</script>
