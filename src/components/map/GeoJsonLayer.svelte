<!-- GeoJsonLayer.svelte -->
<script lang="ts">
  // Types
  interface GeoJSONFeature {
    type: string;
    geometry: {
      type: string;
      coordinates: Array<number>; // TODO: Make this more accurate
    };
    properties?: {
      [key: string]: any;
    };
  }

  // Imports
  import { getContext } from "svelte";
  import L from "leaflet";

  // Props
  export let name: string;
  export let toggleable = true;
  export let options = {};
  export let features: Array<GeoJSONFeature> = [];
  export let setView = false;

  // Get Context
  const { getMap, registerLayer } = getContext("map");
  const map = getMap();

  // Init
  let layer = L.geoJSON(features, options);
  layer.addTo(map);

  // Methods
  function updateLayer(features) {
    layer.clearLayers();
    layer.addData(features);
    if (setView && layer.getLayers().length) {
      map.fitBounds(layer.getBounds());
    }
    if (toggleable) {
      registerLayer(layer, name);
    }
  }

  // Reactivity
  $: updateLayer(features);
</script>
