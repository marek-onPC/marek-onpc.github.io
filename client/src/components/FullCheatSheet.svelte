<script lang="ts">
  export let title: string;
  export let content: string;
  export let language: string;
  export let closeCallback: () => void;

  import Prism from 'prismjs';
  import { fade, scale } from 'svelte/transition';
</script>

<div class="full-cs__outer" in:fade={{ duration: 350 }} out:fade={{ duration: 350, delay: 250 }}>
  <div
    class="full-cs__inner"
    in:scale={{ duration: 350, delay: 250 }}
    out:scale={{ duration: 350 }}
  >
    <h3 class="full-cs__title">
      {title}
    </h3>
    <pre class={`language-${language}`}><code class={`language-${language}`}
        >{@html Prism.highlight(content, Prism.languages[language], language)}</code
      ></pre>
    <button class="button full-cs__button" on:click={closeCallback}>Close</button>
  </div>
</div>

<style lang="scss">
  .full-cs {
    &__outer {
      position: fixed;
      top: 0;
      left: 0;
      background-color: rgba(0, 0, 0, 0.5);
      height: 100vh;
      width: 100vw;
      display: flex;
    }

    &__inner {
      display: flex;
      flex-direction: column;
      margin: 50px;
      padding: 50px;
      height: calc(100vh - 100px);
      width: calc(100vw - 100px);
      box-sizing: border-box;
      background-color: white;
      border: 2px solid #42b883;
      border-radius: 5px;

      pre {
        min-height: calc(100% - 200px) !important;
      }
    }

    &__title {
      font-size: 2rem;
      line-height: 1.167;
      font-weight: 200;
      color: #42b883;
      margin: 0px 0px 25px 0px;
      text-align: center;

      @media (min-width: 600px) {
        font-size: 2.5rem;
      }

      @media (min-width: 900px) {
        font-size: 2.75rem;
      }

      @media (min-width: 1200px) {
        font-size: 3rem;
      }
    }

    &__button {
      margin: auto;
    }
  }
</style>
