<!-- ToolButton.svelte -->
<script lang="ts">
  // Imports
  import { createEventDispatcher } from "svelte";

  // Props
  export let bottom: string;
  export let right = "15px";
  export let zIndex = "2000";

  const dispatch = createEventDispatcher();

  function handleClick() {
    dispatch("click");
  }
</script>

<button
  on:click={handleClick}
  style="bottom: {bottom}; right: {right}; z-index: {zIndex}"
>
  <slot />
</button>

<style lang="scss">
  @import "../../styles/style.scss";

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
    position: absolute;
    box-shadow: 0 0 8px rgba(0, 0, 0, 0.2);
  }
</style>
