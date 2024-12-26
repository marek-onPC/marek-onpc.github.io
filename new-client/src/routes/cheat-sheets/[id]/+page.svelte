<script lang="ts">
  import { page } from '$app/stores';
  import { fetchClientGetWithoutToken } from '$lib/fetchClient';
  import { onMount } from 'svelte';
  import type { CheatSheetWithContentType } from '../../../types.js';
  import Loader from '../../../components/Loader.svelte';

  const cheatSheetId = $page.params.id;
  let cheatSheetData: CheatSheetWithContentType;
  let updatedCheatSheetData: CheatSheetWithContentType;

  const loadCheatSheet = async () => {
    try {
      const cheetSheet = await fetchClientGetWithoutToken(`/cheat_sheets/${cheatSheetId}`);
      cheatSheetData = cheetSheet.data as CheatSheetWithContentType;
    } catch (e) {
      console.log(e);
    }
  };

  onMount(() => {
    loadCheatSheet();
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
          <pre>
            {card.content}
          </pre>
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
