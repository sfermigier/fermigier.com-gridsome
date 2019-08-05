<template>
  <Layout>
    <div class="overflow-x-hidden">
      <div
          class="projects container-inner mx-auto text-xl border-t border-gray-500 border-b py-16 mb-16 relative"
      >
        <h2 class="font-bold mb-6">
          Here are some projects I've worked on:
        </h2>

        <div
            class="absolute right-0"
            style="top: 50px; transform: translate(100%) rotate(180deg);"
        >
          <svg width="170px" height="170px">
            <use xlink:href="#dots-triangle"/>
          </svg>
        </div>

        <div class="content">
          <p>My name is Stefane Fermigier, I'm a tech entrepreneur.</p>

          <p>
            I founded <a href="http://www.nuxeo.com/">Nuxeo</a> in 2000, and served as its CEO from 2000 to 2008, then
            as its executive chairman from 2008 to 2011.
            Nuxeo is now one of the largest open source software vendors in France.</p>

          <p>I've also cofounded several organizations dedicated to developing the open source ecosystem in France:</p>

          <ul>
            <li><a href="http://www.aful.org/">AFUL</a>, the french-speaking Linux and free software users association.
              I served as it president from 1998 to 2003.
            </li>
            <li><a href="http://www.gt-logiciel-libre.org/">GTLL</a>, the business and innovation cluster for open
              source in the Paris Region (part of the Systematic Paris Region cluster). I've bee serving as its
              president since 2009.
            </li>
            <li>The <a href="http://www.openworldforum.org/">Open World Forum</a>, yearly conference dedicated to open
              source and "open everything" in Paris (since 2008). I participated in the organization as the "VP for
              Forum Committee".
            </li>
          </ul>

          <p>I'm also a cofounder of several open source projects:</p>

          <ul>
            <li><a href="http://incubator.apache.org/stanbol/">Apache Stanbol</a></li>
            <li><a href="http://chemistry.apache.org/">Apache Chemistry</a></li>
            <li><a href="http://eclipse.org/apricot/">Eclipse Apricot</a></li>
          </ul>

          <p>I also have a few personal project on <a href="https://github.com/sfermigier">GitHub</a>.</p>

          <h2>Contact &amp; more information</h2>

          <ul>
            <li>Email: sf (at) fermigier.com</li>
            <li>LinkedIn: <a href="http://www.linkedin.com/in/sfermigier">sfermigier</a></li>
            <li>SlideShare: <a href="http://www.slideshare.net/sfermigier/presentations">sfermigier</a></li>
            <li>Twitter: <a href="http://twitter.com/#!/sfermigier">sfermigier</a></li>
            <li>GitHub: <a href="https://github.com/sfermigier">sfermigier</a></li>
            <li>Pinboard: <a href="https://pinboard.in/u:sfermigier/">sfermigier</a></li>
            <li>YouTube: <a href="http://www.youtube.com/user/sfermigier">sfermigier</a></li>
            <li>Goodreads: <a href="http://www.goodreads.com/sfermigier">sfermigier</a></li>
            <li>Google+: <a href="https://plus.google.com/113216181535040193672/posts">sfermigier</a></li>
            <li>Skype: sfermigier</li>
            <li>Instapaper: sfermigier</li>
          </ul>
        </div>

        <ul class="text-lg sm:text-xl">
          <li class="checkmark mb-6">
            <div>Project One</div>
            <div class="text-lg text-gray-600">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui ab
              nam animi iure nemo exercitationem a, eius non culpa itaque!
            </div>
          </li>
          <li class="checkmark mb-6">
            <div>Project Two</div>
            <div class="text-lg text-gray-600">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui ab
              nam animi iure nemo exercitationem a, eius non culpa itaque!
            </div>
          </li>
          <li class="checkmark mb-6">
            <div>Project Three</div>
            <div class="text-lg text-gray-600">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui ab
              nam animi iure nemo exercitationem a, eius non culpa itaque!
            </div>
          </li>
          <li class="checkmark mb-6">
            <div>Project Four</div>
            <div class="text-lg text-gray-600">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui ab
              nam animi iure nemo exercitationem a, eius non culpa itaque!
            </div>
          </li>
        </ul>
      </div>
      <!-- end projects -->
    </div>
  </Layout>
</template>

<script>
  export default {
    metaInfo: {
      title: "Open Source Projects"
    }
  };
</script>
