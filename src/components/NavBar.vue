<template>
  <header class="border-t-14 border-brand-500">
    <nav
      class="container mx-auto flex flex-wrap justify-between items-center py-8"
    >
      <!--      <div :class="isOpen ? 'block' : 'hidden'">-->
      <!--        <g-link v-if="theme === 'theme-light'" to="/" class="text-brand-800">-->
      <!--          <span class="text-3xl font-bold ">-->
      <!--            SF:-->
      <!--          </span>-->
      <!--        </g-link>-->

      <!--        <g-link v-else to="/">-->
      <!--          <span class="text-3xl font-bold ">-->
      <!--            SF:-->
      <!--          </span>-->
      <!--        </g-link>-->
      <!--      </div>-->

      <div class="block lg:hidden">
        <button
          @click="toggle"
          class="flex items-center px-3 py-2 border rounded border-gray-500 hover:text-gray-600 hover:border-gray-600"
        >
          <svg
            class="current-color h-3 w-3"
            viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z" fill="gray" />
          </svg>
        </button>
      </div>

      <ul
        class="uppercase tracking-wide font-bold text-sm	 w-full block flex-grow lg:flex lg:flex-initial lg:w-auto items-center mt-8 lg:mt-0"
        :class="isOpen ? 'block' : 'hidden'"
      >
        <li v-for="entry in menu" class="mr-8 mb-6 lg:mb-0">
          <g-link
            :to="entry.link"
            class="text-copy-primary hover:text-gray-600"
            >{{ entry.label }}</g-link
          >
        </li>
        <li class="mr-8 mb-6 lg:mb-0">
          <search-input />
        </li>
        <!--        <li class="mr-8 mb-6 lg:mb-0">-->
        <!--          <theme-switcher :theme="theme" />-->
        <!--        </li>-->
      </ul>
    </nav>
  </header>
</template>

<script>
import SearchInput from "../components/SearchInput";
import ThemeSwitcher from "../components/ThemeSwitcher";

export default {
  components: {
    SearchInput,
    ThemeSwitcher,
  },

  props: {
    theme: {
      type: String,
      required: true,
    },
  },

  data() {
    return {
      isOpen: false,
      menu: [
        {
          label: "Home",
          link: "/",
        },
        {
          label: "Business",
          link: "/business/",
        },
        {
          label: "Open Source",
          link: "/open-source/",
        },
        {
          label: "Talks",
          link: "/presentations/",
        },
        {
          label: "Writings",
          link: "/writing/",
        },
        // {
        //   label: "About",
        //   link: "/about/",
        // },
        {
          label: "Blog",
          link: "/blog/",
        },
      ],
    };
  },

  methods: {
    toggle() {
      this.isOpen = !this.isOpen;
    },
  },
};
</script>
