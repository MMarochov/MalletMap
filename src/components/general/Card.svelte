<!-- Card.svelte -->
<script lang="ts">
  // Props
  export let title: string;
  export let src: string;
  export let alt: string;
</script>

<div class="card">
  <div>
    <img {src} {alt} />
    <h3>{title}</h3>
  </div>
  <div class="content">
    <slot />
  </div>
</div>

<style lang="scss">
  @import "../../styles/style.scss";


  img {
    background-size: cover;
    width: 100%;
    vertical-align: middle;
  }

  .card {
    max-width: 320px;
  }

  .card > div:first-child {
    position: relative;
  }

  .content {
    padding: 32px;
    color: $color-primary-charcoal;
    background-color: $color-primary-white;
  }

  h3 {
    color: $color-primary-charcoal;
    text-transform: uppercase;
    font-family: $os-gill-regular;
    font-style: normal;
    font-weight: normal;
    font-size: 1.5rem;
    letter-spacing: 4px;
    line-height: 1;
    padding: 8px 16px;
    background: $color-primary-white;
    position: absolute;
    top: auto;
    left: 16px;
    bottom: 16px;
    transform: none;
    margin: 0px;
  }
</style>
