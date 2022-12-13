<!-- App.svelte -->

<script lang="ts">
  // Imports
  import Map from "./components/map/Map.svelte";
  import GeoJsonLayer from "./components/map/GeoJsonLayer.svelte";
  import Marker from "./components/map/Marker.svelte";
  import SidePanel from "./components/general/SidePanel.svelte";
  import Card from "./components/general/Card.svelte";
  import Popup from "./components/general/Popup.svelte";
  import License from "./components/general/License.svelte";
  import { licenseTermsAccepted } from "./stores/licenseStore";
  import {apiKey} from "./config";

  // Init
  let map;
  // let features = [
  //   {
  //     type: "Feature",
  //     properties: {},
  //     geometry: {
  //       type: "Polygon",
  //       coordinates: [
  //         [
  //           [-1.381455659866333, 51.77699819490482],
  //           [-1.3824212551116943, 51.776609859319194],
  //           [-1.3824212551116943, 51.77543819409507],
  //           [-1.3812518119812012, 51.775839816479575],
  //           [-1.381455659866333, 51.77699819490482],
  //         ],
  //       ],
  //     },
  //   },
  // ];
</script>
<License />
<main class="dark {$licenseTermsAccepted ? '' : 'blurry'}">
  
  <Map {apiKey} bind:map>
    <!-- <GeoJsonLayer name="GeoJSON" bind:features />
    <Marker name="Marker" lat={51.776} lon={-1.379} /> -->
  </Map>

  <SidePanel>
    <h2 class="lead-in-subheading light {$licenseTermsAccepted ? '' : 'blurry'}">Welcome to</h2>
    <h1 class="large-subheading light {$licenseTermsAccepted ? '' : 'blurry'}">Timmy Mallett's Map!</h1>
    <p class="light {$licenseTermsAccepted ? '' : 'blurry'}">
      Lorem ipsum, dolor sit amet consectetur adipisicing elit. Maxime voluptate
      libero voluptatem sed reiciendis reprehenderit! Adipisci tempore, mollitia
      voluptatem accusantium sequi consectetur doloremque quasi? Mollitia quis
      voluptate placeat quidem exercitationem! Ut laborum harum maiores id quae
      officiis quos odio error molestiae? Corporis fuga odit dolorum magni at
      hic commodi, nihil necessitatibus dignissimos earum nemo! Ipsa asperiores
      facere corrupti nulla soluta! Assumenda ad magni incidunt voluptas error!
      Corrupti aperiam beatae iusto, quos obcaecati eaque hic aliquam, iste
      voluptatibus dolorum perferendis.
    </p>
  </SidePanel>
  <!-- <Popup>
    <h2 class="subheading">Welcome to Timmy Mallett's Map!</h2>
    <p>
      Info about map
    </p>
  </Popup> -->
</main>

<style lang="scss">
  @import "./styles/style.scss";

  main {
    height: 100%;
    width: 100%;
  }
</style>
<!-- <script lang="ts">
  import Logo from "./components/general/Logo.svelte";
  import License from "./components/general/License.svelte";
  import { licenseTermsAccepted } from "./stores/licenseStore";
  import Map from "./components/map/Map.svelte";
  import { apiKey } from "./config";

  let map;
</script>
<License />
<main class="dark {$licenseTermsAccepted ? '' : 'blurry'}">
    <Map {apiKey} bind:map />
</main>

<style>
    :global(body),
    main {
        height: 100%;
        width: 100%;
        margin: 0;
        padding: 0;
    }

    .blurry {
    filter: blur(5px);
  }
</style> -->