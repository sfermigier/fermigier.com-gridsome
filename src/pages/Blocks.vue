<template>
  <Layout>
    <div class="container-inner mx-auto py-16 content">
      Hello
      <div
        v-for="block in $page.blocks.edges"
        :key="block.id"
        class="post border-gray-400 border-b mb-12"
      >
        <h2 class="text-3xl font-bold">
          <g-link :to="block.node.path" class="text-copy-primary">{{
            block.node.title
          }}</g-link>
        </h2>

        <div class="text-lg mb-4" v-html="block.node.content"/>
      </div>
      <!-- end post -->
    </div>
  </Layout>
</template>

<page-query>
query Blocks ($page: Int) {
  blocks: allBlock (sortBy: "date", order: DESC, perPage: 3, page: $page) @paginate {
    totalCount
    pageInfo {
      totalPages
      currentPage
    }
    edges {
      node {
        id
        title
        content
      }
    }
  }
}
</page-query>

<script>
export default {
  metaInfo: {
    title: "Blocks"
  },
};
</script>
