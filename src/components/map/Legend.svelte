<!-- Legend.svelte -->
<script lang="ts">
  import { licenseTermsAccepted } from "../../stores/licenseStore";
  import SvelteTooltip from "svelte-tooltip";
</script>

<section>
  <h2 class="lead-in-subheading light {$licenseTermsAccepted ? '' : 'blurry'}">
    Symbology
  </h2>
  <div class="legendItem smaller">
    <img src="./routeMarker.png" alt="route symbology" />
    <p class="light {$licenseTermsAccepted ? '' : 'blurry'}">Cycle Route</p>
  </div>
  <div class="legendItem">
    <img src="./clusterMarker.png" alt="marker symbology" />
    <p class="light {$licenseTermsAccepted ? '' : 'blurry'}">
      Paintings and Videos
    </p>
    <SvelteTooltip tip="Click on the icons or zoom in to view more !" bottom>
      <button><span class="material-symbols-outlined">info</span></button>
    </SvelteTooltip>
  </div>
</section>

<style lang="scss">
  @import "../../styles/style.scss";

  section {
    box-shadow: 0 0 8px rgb(0 0 0 / 20%);
    border-left: 4px solid $color-secondary-blue;
    padding: 14px;
  }
  button {
    margin: 0;
    background: $color-primary-white;
    border: $color-primary-white;
    padding: 0;
    display: flex;
    color: $color-neutral-rock;
    border-radius: 50%;
  }

  p {
    margin: 14px;
  }

  h2 {
    margin: 0px 0px 11px 0px;
  }

  .legendItem {
    display: flex;
    flex-direction: row;
    align-items: center;
  }

  img {
    width: 9%;
    border-radius: 50%;
    box-shadow: 0 0 7px rgb(0 0 0 / 30%);
  }

  .smaller {
    width: 90%;
    padding-left: 3px;
  }
</style>
