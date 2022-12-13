<!-- SidePanel.svelte -->
<script lang="ts">
  // Props
  export let closed = false;
  export let zIndex = 2001;

  let toggleClosed = () => {
    closed ? (closed = false) : (closed = true);
  };

  $: side_icon = closed ? "arrow_right" : "arrow_left";
  $: top_icon = closed ? "menu" : "close";
</script>

<div class="panel" style="z-index:{zIndex}">
  <div class="outer-content" class:closed>
    <div class="content">
      <slot />
    </div>
  </div>
  <div class="buffer">
    <button class="side-button" on:click={toggleClosed}>
      <span class="material-symbols-outlined"> {side_icon} </span>
    </button>
  </div>
</div>
<button style="z-index:{zIndex + 1}" class="top-button" on:click={toggleClosed}>
  <span class="material-symbols-outlined"> {top_icon} </span>
</button>

<style lang="scss">
  @import "../../styles/style.scss";

  $shadow: 3px 0 3px rgba(0, 0, 0, 0.1);

  .panel {
    width: fit-content;
    height: 100%;
    box-sizing: border-box;
    position: fixed;
    top: 0;
    left: 0;
    display: flex;
    background: transparent;
  }

  .outer-content,
  .content {
    height: 100%;
    width: 92vw;
    max-width: 500px;
  }

  .outer-content {
    overflow: hidden;
    transition: width 0.5s ease-in-out;
    padding-right: 1px;
    background: transparentize($color-primary-white, 0.05);
    box-shadow: $shadow;
    position: relative;
  }

  .content {
    padding: 50px 30px;
    transition: width 0.8s ease;
    overflow-y: scroll;
    overflow-x: hidden;
    box-sizing: border-box;
  }

  .closed {
    width: 8px;
  }

  .buffer {
    height: 100%;
    display: flex;
    align-items: center;
  }

  .top-button,
  .side-button {
    margin: 0;
    background: $color-primary-white;
    border: $color-primary-white;
  }

  .top-button {
    position: fixed;
    top: 10px;
    left: 10px;
    display: flex;
    box-shadow: 0 0 5px #80808042;
    border: none;
    border-radius: 100%;
    padding: 5px;
    display: none;

    span {
      font-size: 2rem;
    }
  }

  .side-button {
    padding: 0;
    border-radius: 0 6px 6px 0;
    height: 48px;
    box-shadow: $shadow;
    width: 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    z-index: 0;
  }

  .side-button:hover,
  .top-button:hover {
    opacity: 1;
    background: darken($color-primary-white, 5%);
    color: darken($color-primary-charcoal, 20%);
  }

  @include slim-scrollbar;

  @media (max-width: $breakpoint-mobile) {
    .closed {
      width: 0;
    }

    .top-button {
      display: flex;
    }

    .side-button {
      display: none;
    }
  }
</style>
