<!-- TextApp.svelte -->
<script lang="ts">
  // Imports
  import Card from "./components/general/Card.svelte";
  import Popup from "./components/general/Popup.svelte";
  import Logo from "./components/general/Logo.svelte";
</script>

<main>
  <h2 class="lead-in-subheading">This lead-in subheading leads to</h2>
  <h1 class="large-subheading">This Proper Subheading</h1>

  <h1 class="headline">
    Headline with a <br /><span class="highlight">Highlight</span>
  </h1>
  <p class="padded peckline-5">This is a paragraph with a peckline</p>

  <section class="dark">
    <h2 class="subheading">Now Into Dark Mode!</h2>
    <p>Let's see what a <a href="/#">button</a> looks like...</p>
    <button class="button-dark">Press Me</button>
  </section>

  <section>
    <h2 class="subheading">Images</h2>
    <p>We also have an svg store of all the OS logos</p>
    <div class="logos">
      <Logo logo="logo-colour" width="220px"/>
      <Logo logo="logo-dark" width="220px"/>
      <div class="dark">
        <Logo logo="logo-light" width="220px"/>
      </div>
    </div>
    <button class="button">Light Mode Button</button>
  </section>

  <section
    class="dark"
    style="padding: 30px 0; display:flex; flex-direction: row; flex-wrap: wrap; gap: 20px; justify-content: space-around"
  >
    <Card
      src="https://www.ordnancesurvey.co.uk/image-library/banners/environment/river-meandering-aerial-view.x7edd8cdf.jpg?w=500&q=60&f=webp"
      title="Title"
      >Lorem ipsum dolor sit amet consectetur, adipisicing elit. Unde recusandae
      commodi, porro ab veritatis totam aut enim. Maxime praesentium ab dolor
      laborum deleniti autem, aliquam quam veritatis, omnis explicabo expedita!
      <button class="button">Press Me</button>
    </Card>
    <Card
      src="https://www.ordnancesurvey.co.uk/image-library/banners/closeup-checking-data.xc3f8ab25.jpg?w=500&q=60&f=webp"
      title="Title"
      >Lorem ipsum dolor sit amet consectetur, adipisicing elit. Unde recusandae
      commodi, porro ab veritatis totam aut enim. Maxime praesentium ab dolor
      laborum deleniti autem, aliquam quam veritatis, omnis explicabo expedita!
      <button class="button">Press Me</button>
    </Card>
  </section>

  <Popup visible={false} let:toggleVisible>
    <h1 class="large-subheading">This is a popup</h1>
    <p>
      Lorem ipsum dolor, sit amet consectetur adipisicing elit. Molestias
      nesciunt porro incidunt excepturi quod quibusdam veniam minima? Excepturi
      quasi deleniti rem vel ducimus? Sint quia eos magnam fugit quidem
      quibusdam?
    </p>
    <button on:click={toggleVisible} class="button">Get Started</button>
    <button class="button" slot="toggle" on:click={toggleVisible}
      >Show Popup</button
    >
  </Popup>
</main>

<style lang="scss">
  @import "./styles/style.scss";

  main {
    max-width: 800px;
    width: 100%;
    margin: 0 auto;
    padding: 40px 20px;
    box-sizing: border-box;
  }

  section {
    padding: 10px 20px;
  }

  .padded {
    padding: 10px;
  }

  .logos {
    display: flex;
    gap: 10px;
    margin: 10px 0 20px 0;
    flex-wrap: wrap;

    img {
      width: 220px;
    }
  }
</style>
