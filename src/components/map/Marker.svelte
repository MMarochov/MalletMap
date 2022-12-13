<!-- Marker.svelte -->
<script lang="ts">
  // Imports
  import { getContext } from "svelte";
  import L from "leaflet";

  // Props
  export let name: string;
  export let lat: number;
  export let lon: number;
  export let toggleable = true;
  export let options = {};

  // Get Context
  const { getMap, registerLayer } = getContext("map");
  const map = getMap();

  // Init
  let marker;

  // Methods
  function updateMarker(lat: number, lon: number) {
    if (marker) {
      map.removeLayer(marker);
    }
    marker = new L.Marker([lat, lon], options);
    map.addLayer(marker);
    if (toggleable) {
      registerLayer(marker, name);
    }
  }

  // Reactivity
  $: updateMarker(lat, lon);
</script>
