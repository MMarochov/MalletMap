<!-- Map.svelte -->
<script lang="ts">
  // Imports
  import L from "../Leaflet.Photo.js";
  import { onMount, onDestroy, setContext } from "svelte";
  import ToggleButton from "./ToggleButton.svelte";
  import ToolButton from "../general/ToolButton.svelte";
  import VectorTileLayer from "leaflet-vector-tile-layer";
  import { media } from "./media.js";

  // Types
  type OSBaseMap = "Light_3857" | "Outdoor_3857" | "Road_3857";

  // Props
  export let map;
  export let apiKey: string;
  export let map_style: OSBaseMap = "Outdoor_3857";
  export let center: [number, number] = [52.276, -6.479];
  export let zoom = 7;
  export let showToggle = true;
  export let options = { zoomControl: false, minZoom: 7 };
  export let height = "100%";
  export let width = "100%";

  // Init: Basemap
  let container: HTMLDivElement;
  let layers = {};
  let year = new Date().getFullYear();
  let attribution = `Contains OS data &copy Crown copyright and database rights ${year}`;
  let datahubEndpoint = `https://api.os.uk/maps/raster/v1/zxy/${map_style}/{z}/{x}/{y}.png?key=${apiKey}`;
  let tileLayer = L.tileLayer(datahubEndpoint, { attribution: attribution });
  let layerControlVisible = false;

  // Innit: Media
  let mediaLayer = L.photo.cluster().on("click", function (evt) {
    let photo = evt.layer.photo;
    let template;
    if (photo.type == "image") {
      template = `<img class="popup" src="${photo.url}" /></a><h3>${photo.name}</h3><p>${photo.description}</p>`;
    } else {
      template = `<iframe width="450" height="315" src="https://www.youtube.com/embed/${photo.id}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>`;
    }
    evt.layer.bindPopup(L.Util.template(template, photo)).openPopup();
  });

  // Init: cycle gpx vector tile
  let url = "https://labs.os.uk/tiles/vector/mallett-gpx-route/{z}/{x}/{y}.pbf";
  let vtileOptions = {
    layers: ["gpx-track"],
    maxDetailZoom: 14,
    style: { color: "#d20e58", weight: 4, opacity: 0.8, interactive: false },
  };
  let vtileLayer = VectorTileLayer(url, vtileOptions);

  // Render Map
  onMount(() => {
    map = L.map(container, options).setView(L.latLng(...center), zoom);
    tileLayer.addTo(map);
    vtileLayer.addTo(map);
    mediaLayer.add(media).addTo(map);
  });

  // Remove Map
  onDestroy(() => {
    if (map) map.remove();
  });

  // Set Context
  setContext("map", {
    getMap: () => map,
    registerLayer: (layer, name: string) => {
      layers[name] = layer;
      layers = layers;
    },
  });

  // Methods
  function toggleLayer(layer): void {
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
    background: #a9ddef;
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
    border: 4px solid #ff5f00c4 !important;
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
    width: 450px !important;
  }

  :global(.leaflet-popup-content) {
    margin: 16px !important;
    & :global(h3) {
      margin: 15px 0 6px 0 !important;
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
    background: $color-secondary-orange;
    height: 32px;
    width: 32px;
    border-radius: 50%;
    font-weight: bold;
    font-size: 15px;
  }

  :global(.leaflet-marker-photo) {
    border-radius: 50%;
    background: #fab58f;
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
