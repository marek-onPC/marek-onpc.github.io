<script lang="ts">
  import { fetchClientGet } from '$lib/fetchClient';
  import { onMount } from 'svelte';
  import type { CheatSheetWithContentType } from '../../types';
  import { sessionToken } from '../../stores';
  import Card from '../../components/Card.svelte';
  import Loader from '../../components/Loader.svelte';

  let cheatSheetsData: Array<CheatSheetWithContentType>;

  const loadCheatSheets = async () => {
    try {
      const raw = await fetchClientGet('/cheat_sheets', $sessionToken);
      cheatSheetsData = JSON.parse(raw.data) as Array<CheatSheetWithContentType>;
    } catch (e) {
      console.log(e);
    }
  };

  onMount(() => {
    loadCheatSheets();
  });
</script>

<div class="dashboard-list">
  {#if cheatSheetsData}
    {#each cheatSheetsData as card}
      <a href={`/dashboard/cheat-sheet/${card.id}`}><Card cheatSheetData={card} /></a>
    {/each}
  {:else}
    <Loader />
  {/if}
</div>

<style lang="scss">
  .dashboard-list {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;

    a {
      text-decoration: inherit;
      color: inherit;
      cursor: auto;
    }
  }
</style>
