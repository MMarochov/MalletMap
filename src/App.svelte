<!-- App.svelte -->
<script lang="ts">
  // Imports
  import Map from "./components/map/Map.svelte";
  import Legend from "./components/map/Legend.svelte";
  import SidePanel from "./components/general/SidePanel.svelte";
  import Logo from "./components/general/Logo.svelte";
  import License from "./components/general/License.svelte";
  import { licenseTermsAccepted } from "./stores/licenseStore";
  import { apiKey } from "./config";

  // Init
  let map;
</script>

<License />
<main class="dark {$licenseTermsAccepted ? '' : 'blurry'}">
  <Map {apiKey} bind:map />

  <SidePanel>
    <Logo logo="logo-colour" width={"150px"} />
    <div id="title">
      <h2
        class="lead-in-subheading padded peckline-5 light {$licenseTermsAccepted
          ? ''
          : 'blurry'}"
      >
        Painting Utterly Brilliant Britain
      </h2>
      <h1 class="headline light {$licenseTermsAccepted ? '' : 'blurry'}">
        Timmy Mallett's
      </h1>
      <h2 class="headline-2 light {$licenseTermsAccepted ? '' : 'blurry'}">
        Cycling Circumnavigation of GB
      </h2>
    </div>
    <h2
      class="lead-in-subheading light {$licenseTermsAccepted ? '' : 'blurry'}"
    >
      The origin story
    </h2>
    <p class="light {$licenseTermsAccepted ? '' : 'blurry'}">
      I’m curious about our country. Among the consequences of the pandemic and
      Brexit has been my increased interest in the British Isles, and what there
      is to explore and discover.
    </p>
    <p class="light {$licenseTermsAccepted ? '' : 'blurry'}">
      This story starts over 200 years ago when Napoleon discouraged people from
      travelling to Europe, and artists like the national treasure, Joseph
      Turner, set off to explore Britain with their sketchbooks.
    </p>
    <p class="light {$licenseTermsAccepted ? '' : 'blurry'}">
      I wanted to explore the coast of the UK by bike and paint the adventure as
      I went. I hoped to see and paint many of Joseph Turner’s great coastal
      scenes along the way. To this end, Ordnance Survey stepped in with
      their great range of maps to help with planning and choosing good cycle
      routes.
    </p>
    <p class="light {$licenseTermsAccepted ? '' : 'blurry'}">
      I’m inspired by my brother Martin who has Down syndrome, to aim high and
      see what’s achievable. I expected this journey to be around 4,500 miles
      over at least 3 months.
    </p>
    <p class="light {$licenseTermsAccepted ? '' : 'blurry'}">
      I planned to start in Spring. I set the start date one boiling hot day in July and put it in the diary so there was something concrete to aim for.
      Eight months later was Thursday March 17th – St Patrick’s Day. That
      sounded about right.
    </p>
    <p class="light {$licenseTermsAccepted ? '' : 'blurry'}">
      I set off from Paddington Station down the Thames, and then headed
      clockwise around the coast, keeping the sea on my left...
    </p>
    <h2
      id="author"
      class="lead-in-subheading light {$licenseTermsAccepted ? '' : 'blurry'}"
    >
      ~ Timmy Mallett
    </h2>
    <Legend />
  </SidePanel>
</main>

<style lang="scss">
  @import "./styles/style.scss";
  main {
    height: 100%;
    width: 100%;
  }

  .padded {
    padding: 8px;
  }

  #author {
    text-align: right;
    margin: 20px 0px 20px 0px;
  }

  #title {
    margin-bottom: 27px;
  }

  h1 {
    margin: 15px 0px 15px 0px;
  }
  :global(.headline-2) {
    font-size: 27px;
    font-family: "OS Gill Regular", sans-serif;
  }
</style>
