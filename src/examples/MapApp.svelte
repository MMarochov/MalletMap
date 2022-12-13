<!-- MapApp.svelte -->
<script lang="ts">
  // Imports
  import Map from "./components/map/Map.svelte";
  import GeoJsonLayer from "./components/map/GeoJsonLayer.svelte";
  import Marker from "./components/map/Marker.svelte";
  import SidePanel from "./components/general/SidePanel.svelte";
  import Card from "./components/general/Card.svelte";
  import Popup from "./components/general/Popup.svelte";
  import {apiKey} from "./config";

  // Init
  let map;
  let features = [
    {
      type: "Feature",
      properties: {},
      geometry: {
        type: "Polygon",
        coordinates: [
          [
            [-1.381455659866333, 51.77699819490482],
            [-1.3824212551116943, 51.776609859319194],
            [-1.3824212551116943, 51.77543819409507],
            [-1.3812518119812012, 51.775839816479575],
            [-1.381455659866333, 51.77699819490482],
          ],
        ],
      },
    },
  ];
</script>

<main>
  <Map {apiKey} bind:map>
    <GeoJsonLayer name="GeoJSON" bind:features />
    <Marker name="Marker" lat={51.776} lon={-1.379} />
  </Map>

  <SidePanel>
    <h2 class="lead-in-subheading">We also have a</h2>
    <h1 class="large-subheading">Sidebar Component</h1>
    <p>
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
    <p>
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
    <div
      class="dark"
      style="padding: 40px 10px; display: flex; justify-content: center"
    >
      <Card
        src="https://www.ordnancesurvey.co.uk/image-library/banners/closeup-checking-data.xc3f8ab25.jpg?w=500&q=60&f=webp"
        title="Title"
        >Lorem ipsum dolor sit amet consectetur, adipisicing elit. Unde
        recusandae commodi, porro ab veritatis totam aut enim. Maxime
        praesentium ab dolor laborum deleniti autem, aliquam quam veritatis,
        omnis explicabo expedita!
        <button class="button">Press Me</button>
      </Card>
    </div>
  </SidePanel>
  <Popup>
    <h2 class="subheading">Map Popup</h2>
    <p>
      This map popup is visible by default and uses the default toggle button,
      which you can see in the bottom right-hand corner of the screen!
    </p>
  </Popup>
</main>

<style lang="scss">
  @import "./styles/style.scss";

  main {
    height: 100%;
    width: 100%;
  }
</style>