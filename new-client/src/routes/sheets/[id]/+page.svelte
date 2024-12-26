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
    {/if}
  {:else}
    <Loader />
  {/if}
</div>

<style lang="scss">
  .sheet {
  }
</style>
