<!-- Logo.svelte -->
<script lang="ts">
  // Types
  type LogoName =
    | "logo-colour"
    | "logo-dark"
    | "logo-light"
    | "logo-strapline-colour"
    | "logo-strapline-dark"
    | "logo-strapline-light"
    | "logomark-colour"
    | "logomark-dark"
    | "logomark-light";

  // Props
  export let width = "auto";
  export let height = "auto";
  export let logo: LogoName;
</script>

<img src="./logos/{logo}.svg" {width} {height} alt="Ordnance Survey Logo" />

<style>
  img {
    margin-bottom: 20px;
  }
</style>