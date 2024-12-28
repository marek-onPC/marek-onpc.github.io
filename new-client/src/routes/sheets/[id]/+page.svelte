<script lang="ts">
  import { page } from '$app/stores';
  import { fetchClientGetWithoutToken } from '$lib/fetchClient';
  import { onMount } from 'svelte';
  import type { CheatSheetWithContentType } from '../../../types.js';
  import Loader from '../../../components/Loader.svelte';

  // Prism
  import '../[id]/prism.css';
  import Prism from 'prismjs';
  import 'prismjs/components/prism-python.js';
  import 'prismjs/components/prism-javascript.js';
  import 'prismjs/components/prism-jsx.js';
  import 'prismjs/components/prism-typescript.js';
  import 'prismjs/components/prism-tsx.js';
  import 'prismjs/components/prism-swift.js';
  import 'prismjs/components/prism-css.js';
  import 'prismjs/components/prism-scss.js';

  const cheatSheetId = $page.params.id;
  let cheatSheetData: CheatSheetWithContentType;
  let language = 'python';

  const loadCheatSheet = async () => {
    try {
      const cheetSheet = await fetchClientGetWithoutToken(`/cheat_sheets/${cheatSheetId}`);
      cheatSheetData = cheetSheet.data as CheatSheetWithContentType;
    } catch (e) {
      console.log(e);
    }
  };

  onMount(async () => {
    await loadCheatSheet();
  });
</script>

<div class="sheet__page">
  {#if cheatSheetData}
    <h1 class="sheet__title">
      {cheatSheetData.title}
    </h1>
    {#if cheatSheetData.cards}
      <div class="sheet__cards">
        {#each cheatSheetData.cards as card}
          <div class="sheet__card-wrapper">
            <h3 class="sheet__card-title">
              {card.subtitle}
            </h3>
            <pre class="language-python"><code class="language-python"
                >{@html Prism.highlight(card.content, Prism.languages[language], language)}</code
              ></pre>
          </div>
        {/each}
      </div>
    {/if}
  {:else}
    <Loader />
  {/if}
</div>

<style lang="scss">
  .sheet {
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

    &__cards {
      display: flex;
      flex-wrap: wrap;
    }

    &__card-wrapper {
      display: flex;
      flex-direction: column;
      width: 100%;
      background-color: #fff;
      padding: 15px;
      margin: 10px;
      border-radius: 5px;
      border: 2px solid #fff;
      transition: 0.25s ease-in-out;
      position: relative;

      @media (min-width: 600px) {
        width: calc(50% - 54px);
      }

      &:hover {
        border: 2px solid #42b883;

        .sheet__card-title {
          color: #42b883;
        }
      }
    }

    &__card-title {
      font-weight: 400;
      font-size: 20px;
      margin-top: 0;
      margin-bottom: 10px;
      padding-bottom: 10px;
      border-bottom: 1px solid #42b883;
      transition: 0.25s ease-in-out;
    }
  }
</style>
