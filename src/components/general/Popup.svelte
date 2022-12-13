<!-- Popup.svelte -->
<script lang="ts">
  // Imports
  import { fade } from "svelte/transition";
  import ToolButton from "./ToolButton.svelte";

  // Props
  export let visible = true;
  export let zIndex = 2002;

  let toggleVisible = () => {
    visible = visible ? false : true;
  };
</script>

{#if visible}
  <div
    id="container"
    style="z-index:{zIndex}"
    in:fade={{ duration: 100 }}
    out:fade={{ duration: 100 }}
  >
    <div id="content-wrapper">
      <div id="content">
        <button id="close" on:click={toggleVisible} >
          <span class="material-symbols-outlined"
            >close</span
          >
        </button>
        <slot {toggleVisible} />
      </div>
    </div>
  </div>
{/if}

<slot name="toggle" {toggleVisible}>
  <ToolButton on:click={toggleVisible} bottom="30px">
    <span class="material-symbols-outlined">info</span>
  </ToolButton>
</slot>

<style lang="scss">
  @import "../../styles/style.scss";

  #container {
    position: fixed;
    align-items: center;
    justify-content: center;
    display: flex;
    background: rgba(0, 0, 0, 0.5);
    inset: 0 0 0 0;
  }

  #content-wrapper {
    position: relative;
    width: 100%;
    max-width: 30rem;
    height: 30rem;
    background: $color-primary-white;
    border-radius: 10px;
    padding: 30px;
    margin: 10px;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.4), 0 0 15px rgba(0, 0, 0, 0.2),
      0 0 30px rgba(0, 0, 0, 0.1);
  }

  #content {
    height: 100%;
    overflow-y: scroll;
    padding: 10px;
  }

  button {
    border: none;
    border-radius: 100%;
    margin: 0;
    width: 40px;
    height: 40px;
    padding: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    background: transparentize($color-primary-white, 0.2);
  }

  #close {
    position: absolute;
    right: 10px;
    top: 10px;
    background: $color-primary-white;
  }

  @include slim-scrollbar;
</style>
