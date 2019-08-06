<template>
  <Layout>
    <div class="overflow-x-hidden">
      <div
        class="projects container-inner mx-auto text-xl border-t border-gray-500 border-b py-16 mb-16 relative"
      >
        <div class="content">
          <h1>{{ $page.block.title }}</h1>

          <div v-html="$page.block.content"></div>
        </div>
      </div>
    </div>
  </Layout>
</template>

<page-query>
query Block {
  block (path: "/blocks/business") {
    title
    content
  }
}
</page-query>
