<script>
  // Import
  import { licenseTermsAccepted } from "../../stores/licenseStore";
  import Popup from "./Popup.svelte";
  import ToolButton from "./ToolButton.svelte";

  function acceptTerms() {
    $licenseTermsAccepted = true;
    toggleVisible();
  }
</script>

{#if !$licenseTermsAccepted}
  <Popup let:toggleVisible>
    <h2>
      <span class="material-symbols-outlined">policy</span> License Agreement
    </h2>
    <ul>
      <li>
        The mapping data is provided for your personal and/or non-commercial
        use, solely to assist you in understanding and visualising how the code
        operates (the Purpose).
      </li>
      <li>
        You are granted a non-exclusive, royalty free, revocable licence solely
        to view the mapping data for the Purpose, for the period during which
        Ordnance Survey makes it available.
      </li>
      <li>
        You are not permitted to copy, sub-license, distribute, sell or
        otherwise make available the Licensed Data to third parties in any form.
      </li>
      <li>
        You are not permitted to create any products or services which have
        benefitted from, relied on or made any use of the mapping data
        (including, without limitation, where you have created your products or
        services by copying, publishing, modifying, re-formatting, analysing or
        performing searches, look ups or enquiries using the mapping data).
      </li>
      <li>
        Third party rights to enforce the terms of this licence shall be
        reserved to Ordnance Survey.
      </li>
    </ul>
    <div>
      <button class="button" on:click={acceptTerms}>Accept</button>
      <button class="button-alt" on:click={toggleVisible}>Reject</button>
    </div>

    <div slot="toggle">
      <slot name="toggle">
        {#if !$licenseTermsAccepted}
          <ToolButton on:click={toggleVisible} bottom="30px">
            <span id="icon-license" class="material-symbols-outlined"
              >policy</span
            >
          </ToolButton>
        {/if}
      </slot>
    </div>
  </Popup>
{/if}

<style lang="scss">
  @import "../../styles/style.scss";

  div {
    text-align: center;
    margin-top: 30px;
  }

  h2 span {
    vertical-align: bottom;
  }
</style>
