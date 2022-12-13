<!-- Map.svelte -->
<script lang="ts">
  // Imports
  import L from "leaflet";
  import { onMount, onDestroy, setContext } from "svelte";
  import ToggleButton from "./ToggleButton.svelte";
  import ToolButton from "../general/ToolButton.svelte";

  // Types
  type OSBaseMap = "Light_3857" | "Outdoor_3857" | "Road_3857";

  // Props
  export let map;
  export let apiKey: string;
  export let map_style: OSBaseMap = "Outdoor_3857";
  export let center: [number, number] = [51.776, -1.379];
  export let zoom = 16;
  export let showToggle = true;
  export let options = { zoomControl: false };
  export let height = "100%";
  export let width = "100%";

  // Init
  let container: HTMLDivElement;
  let layers = {};
  let year = new Date().getFullYear();
  let attribution = `Contains OS data &copy Crown copyright and database rights ${year}`;
  let datahubEndpoint = `https://api.os.uk/maps/raster/v1/zxy/${map_style}/{z}/{x}/{y}.png?key=${apiKey}`;
  let tileLayer = L.tileLayer(datahubEndpoint, {attribution: attribution });
  let layerControlVisible = false;

  // Render Map
  onMount(() => {
    map = L.map(container, options).setView(L.latLng(...center), zoom);
    tileLayer.addTo(map);
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
</svelte:head>

<div bind:this={container} style="width: {width}; height: {height}">
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
