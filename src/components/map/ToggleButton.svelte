<!-- ToggleButton.svelte -->
<script lang="ts">
  // Imports
  import { createEventDispatcher } from "svelte";

  // Props
  export let on = true;
  export let color = "#333333";

  // Event Dispatch
  const dispatch = createEventDispatcher();

  function handleClick() {
    on = on ? false : true;
    dispatch("toggle", {});
  }
</script>

<button class:on on:click={handleClick} style="--color: {color}">
  <div id="circles">
    <div />
    <div />
  </div>
  <slot />
</button>

<style lang="scss">
  @import "../../styles/style.scss";

  button {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 8px 12px;
    width: fit-content;
    min-width: 160px;
    font-family: inherit;
    border: none;
    border-radius: 4px;
    background: transparent;
    border: 2px solid $color-primary-charcoal;
  }

  #circles {
    width: 20px;
    height: 20px;
    border-radius: 100%;
    position: relative;
  }

  #circles div:first-child {
    border-radius: 100%;
    position: absolute;
    background: transparent;
    border: 2px solid var(--color);
    box-sizing: border-box;
    width: 100%;
    height: 100%;
  }

  #circles div:last-child {
    border-radius: 100%;
    position: absolute;
    background: transparent;
    width: 10px;
    height: 10px;
    top: 5px;
    left: 5px;
    transition: background 0.4s;
  }

  .on #circles div:last-child {
    background: var(--color);
  }
</style>
