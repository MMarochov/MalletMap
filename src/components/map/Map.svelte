<!-- Map.svelte -->
<script lang="ts">
  // Imports
  import L from "../Leaflet.Photo.js";
  import omnivore from "@mapbox/leaflet-omnivore";
  import { onMount, onDestroy, setContext } from "svelte";
  import ToggleButton from "./ToggleButton.svelte";
  import ToolButton from "../general/ToolButton.svelte";

  // Types
  type OSBaseMap = "Light_3857" | "Outdoor_3857" | "Road_3857";

  // Props
  export let map;
  export let apiKey: string;
  export let map_style: OSBaseMap = "Light_3857";
  export let center: [number, number] = [51.676, -2.279];
  export let zoom = 8;
  export let showToggle = true;
  export let options = { zoomControl: false, minZoom: 7 };
  export let height = "100%";
  export let width = "100%";

  // Init
  let container: HTMLDivElement;
  let layers = {};
  let year = new Date().getFullYear();
  let attribution = `Contains OS data &copy Crown copyright and database rights ${year}`;
  let datahubEndpoint = `https://api.os.uk/maps/raster/v1/zxy/${map_style}/{z}/{x}/{y}.png?key=${apiKey}`;
  let tileLayer = L.tileLayer(datahubEndpoint, { attribution: attribution });
  let layerControlVisible = false;
  let photos = [
    {
      lat: 51.50066871058191,
      lng: -0.05953616174794717,
      thumbnail:
        "./data/Paintings/1. Tower Bridge from Bermondsey Angel Inn.jpg",
      url: "./data/Paintings/1. Tower Bridge from Bermondsey Angel Inn.jpg",
      name: "Tower Bridge and the City of London",
      description:
        "My last look back at the City of London in the Spring sunshine.",
    },
    {
      lat: 51.39733171237847,
      lng: 0.5040850096976737,
      thumbnail: "./data/Paintings/3  Rochester along the Medway.jpg",
      url: "./data/Paintings/3  Rochester along the Medway.jpg",
      name: "Medway Magic",
      description:
        "The mighty Medway in the early evening light. This is a skyline that has barely changed in centuries. It’s still dominated by the cathedral and the castle.",
    },
    {
      lat: 51.277863882260824,
      lng: 1.1828876212767603,
      thumbnail: "./data/Paintings/5a  Kent oasthouses at  Ickham.jpg",
      url: "./data/Paintings/5a  Kent oasthouses at  Ickham.jpg",
      name: "Quintessentially Kent",
      description:
        "These four oast houses are quintessentially Kent. They are opposite the wonderful ancient church in the village of Ickham.",
    },
    {
      lat: 51.374929358508545,
      lng: 1.445630037670987,
      thumbnail: "./data/Paintings/5c North Foreland Lighthouse.jpg",
      url: "./data/Paintings/5c North Foreland Lighthouse.jpg",
      name: "North Foreland Lighthouse",
      description:
        "This is one of the stunning squat stone lighthouses built to protect shipping coming around the coast into the Dover Straits. I always knew I’d stop and sketch it. I didn’t expect it to be in such a bright blue spring sky.",
    },
    {
      lat: 51.13003543233797,
      lng: 1.332512374861635,
      thumbnail: "./data/Paintings/6a Dover Castle.jpg",
      url: "./data/Paintings/6a Dover Castle.jpg",
      name: "Dover Castle ",
      description:
        "It’s hard to get a good view of Dover Castle from the west. This was my glimpse of the great structure from the top of Dame Vera Lynne way.",
    },
  ];
  let photoLayer = L.photo.cluster().on("click", function (evt) {
    let photo = evt.layer.photo;
    let template =
      '<img class="popup" src="{url}" /></a><h3>{name}</h3><p>{description}</p>';
    evt.layer.bindPopup(L.Util.template(template, photo)).openPopup();
  });

  // Render Map
  onMount(() => {
    map = L.map(container, options).setView(L.latLng(...center), zoom);
    tileLayer.addTo(map);
    omnivore
      .geojson("./data/Processed/gpx_track_lines_processed_diss.geojson")
      .addTo(map);
    photoLayer.add(photos).addTo(map);
  });

  // Remove Map
  onDestroy(() => {
    if (map) map.remove();
  });

  // Set Context
  setContext("map", {
    getMap: () => map,
    registerLayer: (layer, name: string) => {
      // TODO: Add layer type
      layers[name] = layer;
      layers = layers;
    },
  });

  // Methods
  function toggleLayer(layer): void {
    // TODO: Add layer type
    map.hasLayer(layer) ? map.removeLayer(layer) : layer.addTo(map);
  }

  function toggleLayerControls() {
    layerControlVisible = !layerControlVisible;
  }
</script>

<svelte:head>
  <link
    rel="stylesheet"
    href="https://unpkg.com/leaflet@1.6.0/dist/leaflet.css"
    integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ=="
    crossorigin=""
  />
  <script
    src="https://cdnjs.cloudflare.com/ajax/libs/leaflet-ajax/2.1.0/leaflet.ajax.min.js"
  ></script>
</svelte:head>

<div
  bind:this={container}
  id="map-container"
  style="width: {width}; height: {height}"
>
  {#if map}
    <slot />
  {/if}
</div>

{#if showToggle && Object.keys(layers).length > 0}
  <ToolButton on:click={toggleLayerControls} bottom="80px">
    <span class="material-symbols-outlined">layers</span>
  </ToolButton>

  <div id="layer-toggle" style={layerControlVisible ? "" : "display:none"}>
    <button id="layer-close" on:click={toggleLayerControls}>
      <span class="material-symbols-outlined">close</span>
    </button>
    <h4>Layer Controls</h4>
    {#each Object.entries(layers) as [name, layer]}
      <ToggleButton on:toggle={() => toggleLayer(layer)}>{name}</ToggleButton>
    {/each}
  </div>
{/if}

<style lang="scss">
  @import "../../styles/style.scss";

  #map-container {
    background: #d2d9da;
  }

  :global(.image-marker) {
    height: 100%;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    & :global(img) {
      width: 100%;
      height: 100%;
      object-fit: cover;
      flex-shrink: 0;
      min-width: 100%;
      min-height: 100%;
      border-radius: 5px;
    }
  }

  :global(.leaflet-div-icon) {
    border-radius: 10px;
    border: 4px solid $color-secondary-blue !important;
    box-shadow: 0px 1px 30px 0px, #000 0px 1px 6px 0px;
  }

  :global(.popup) {
    height: 100%;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    & :global(img) {
      width: 100%;
      height: 100%;
      object-fit: cover;
      flex-shrink: 0;
      min-width: 100%;
      min-height: 100%;
    }
  }
  :global(.leaflet-popup-content-wrapper) {
    border-radius: 8px !important;
  }

  :global(.leaflet-popup-content) {
    margin: 16px !important;
    & :global(h3) {
      margin: 15px 0 10px 0 !important;
    }
    & :global(p) {
      margin: 0 0 6px 0 !important;
    }
    & :global(img) {
      border-radius: 8px !important;
    }
  }
  
  :global(.cluster-marker) {
    display: flex;
    justify-content: center;
    align-items: center;
    background: $color-secondary-blue;
    height: 32px;
    width: 32px;
    border-radius: 50%;
    font-weight: bold;
  }

  :global(.leaflet-marker-photo) {
    border-radius: 50%;
    background: #79caf6;
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    box-shadow: 0px 1px 30px 0px, #000 0px 1px 6px 0px;
  }

  :global(.leaflet-interactive) {
    stroke: $color-secondary-pink;
  }

  #layer-toggle {
    z-index: 2000;
    position: absolute;
    inset: auto 70px 120px auto;

    display: flex;
    flex-direction: column;
    gap: 10px;

    background: rgba(255, 255, 255, 0.8);
    padding: 20px;

    box-shadow: 0 0 8px rgba(0, 0, 0, 0.2);
    border-radius: 5px;

    h4 {
      margin: 0 0 5px;
      text-align: center;
    }
  }

  #layer-controls {
    z-index: 2000;
    position: absolute;
    inset: auto 15px 80px auto;
  }

  #layer-close {
    position: absolute;
    left: 10px;
    top: 10px;
    border: none;
    border-radius: 100%;
    background: transparent;
    padding: 0;
    width: 25px;
    height: 25px;
  }
</style>
