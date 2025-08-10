<script lang="ts">
  import { page } from '$app/stores';
  import { fetchClientGet } from '$lib/fetchClient';
  import { onMount } from 'svelte';
  import type { CheatSheetContent, CheatSheetWithContentType } from '../../../types.js';
  import Loader from '../../../components/Loader.svelte';

  // Prism
  import '../[id]/prism.css';
  import Prism from 'prismjs';
  import 'prismjs/components/prism-markup.js';
  import 'prismjs/components/prism-markdown.js';
  import 'prismjs/components/prism-python.js';
  import 'prismjs/components/prism-javascript.js';
  import 'prismjs/components/prism-jsx.js';
  import 'prismjs/components/prism-typescript.js';
  import 'prismjs/components/prism-tsx.js';
  import 'prismjs/components/prism-swift.js';
  import 'prismjs/components/prism-css.js';
  import 'prismjs/components/prism-scss.js';
  import 'prismjs/components/prism-go.js';
  import 'prismjs/components/prism-java.js';
  import 'prism-svelte';
  import FullCheatSheet from '../../../components/FullCheatSheet.svelte';
  import { isSafari, sessionToken } from '../../../stores.js';

  const cheatSheetId = $page.params.id;
  let cheatSheetData: CheatSheetWithContentType;
  let language: string = 'markup';
  let showFullCheatSheet: boolean = false;
  let fullCheatSheetData: CheatSheetContent = { subtitle: '', content: '' };

  const loadCheatSheet = async () => {
    try {
      const cheatSheet = await fetchClientGet(
        `/cheat_sheets/${cheatSheetId}`,
        $sessionToken.accessToken
      );
      cheatSheetData = cheatSheet.data as CheatSheetWithContentType;
      language = cheatSheetData.language ? cheatSheetData.language : 'markup';
    } catch (e) {
      console.log(e);
    }
  };

  const openFullCheatSheetModal = ({ subtitle, content }: CheatSheetContent) => {
    fullCheatSheetData = {
      subtitle,
      content
    };
    showFullCheatSheet = true;
    document.body.classList.add('--no-scroll');
  };

  const closeFullCheatSheetModal = () => {
    fullCheatSheetData = {
      subtitle: '',
      content: ''
    };
    showFullCheatSheet = false;
    document.body.classList.remove('--no-scroll');
  };

  onMount(async () => {
    await loadCheatSheet();
    console.log(isSafari)
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
            <div class="sheet__card-title">
              <h3>{card.subtitle}</h3>
              <button
                class={`button sheet__card-button ${$isSafari ? '--safari' : ''}`}
                on:click={() =>
                  openFullCheatSheetModal({ subtitle: card.subtitle, content: card.content })}
                >❏</button
              >
            </div>

            <pre class={`language-${language}`}><code class={`language-${language}`}
                >{@html Prism.highlight(card.content, Prism.languages[language], language)}</code
              ></pre>
          </div>
        {/each}
      </div>
      {#if showFullCheatSheet}
        <FullCheatSheet
          title={fullCheatSheetData.subtitle}
          content={fullCheatSheetData.content}
          {language}
          closeCallback={closeFullCheatSheetModal}
        />
      {/if}
    {/if}
  {:else}
    <Loader />
  {/if}
</div>

<style lang="scss">
  .sheet {
    &__page {
      width: 100%;
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

    &__cards {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
    }

    &__card-wrapper {
      display: flex;
      flex-direction: column;
      width: calc(100% - 54px);
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

      @media (min-width: 1200px) {
        width: calc(29%);
      }

      &:hover {
        border: 2px solid #42b883;

        .sheet__card-title {
          color: #42b883;
        }
      }
    }

    &__card-title {
      display: flex;
      justify-content: space-between;
      border-bottom: 1px solid #42b883;

      h3 {
        width: 100%;
        font-weight: 400;
        font-size: 20px;
        margin-top: 0;
        margin-bottom: 10px;
        margin-right: 15px;
        padding-bottom: 10px;
        transition: 0.25s ease-in-out;
      }
    }

    &__card-button {
      height: 32px !important;
      width: 34px;
      font-size: 24px;
      font-weight: 800;
      line-height: 22px;
      padding: 0px 0px 0px 0;

      &.--safari {
        font-size: 32px;
        padding: 0px 0px 8px 0;
      }
    }
  }
</style>
