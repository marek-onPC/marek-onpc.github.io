<script lang="ts">
  import { fetchClientGetWithoutToken } from '$lib/fetchClient';
  import { onMount } from 'svelte';
  import type { CheatSheetWithContentType } from '../../types';
  import Card from '../../components/Card.svelte';
  import Loader from '../../components/Loader.svelte';

  let cheatSheetsData: Array<CheatSheetWithContentType>;

  const loadCheatSheets = async () => {
    try {
      const raw = await fetchClientGetWithoutToken('/cheat_sheets');
      cheatSheetsData = raw.data as Array<CheatSheetWithContentType>;
    } catch (e) {
      console.log(e);
    }
  };

  onMount(() => {
    loadCheatSheets();
  });
</script>

<div class="list">
  {#if cheatSheetsData}
    {#each cheatSheetsData as card}
      <a href={`/sheets/${card.id}`}><Card cheatSheetData={card} /></a>
    {/each}
  {:else}
    <Loader />
  {/if}
</div>

<style lang="scss">
  .list {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-content: flex-start;

    a {
      text-decoration: inherit;
      color: inherit;
      cursor: auto;
      width: 100%;
      max-width: 300px;
    }
  }
</style>
