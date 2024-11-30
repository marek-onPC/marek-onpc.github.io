<script lang="ts">
  import { fetchClientGet } from '$lib/fetchClient';
  import { onMount } from 'svelte';
  import type { CheatSheetWithContentType } from '../../types';
  import { sessionToken } from '../../stores';
  import Card from '../../components/Card.svelte';

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

<div>
  {#if cheatSheetsData}
    {#each cheatSheetsData as card}
      <Card cheatSheetData={card} />
    {/each}
  {:else}
    <p>Loading...</p>
  {/if}
</div>
