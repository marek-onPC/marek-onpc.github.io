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
      const raw = await fetchClientGet('/cheat_sheets', $sessionToken.accessToken, {
        is_published__list: [true, false]
      });
      cheatSheetsData = raw.data as Array<CheatSheetWithContentType>;
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
      <a href={`/dashboard/cs-edit/${card.id}`}
        ><Card cheatSheetData={card} showShowStatus={true} /></a
      >
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
      width: 100%;
      max-width: 300px;
    }
  }
</style>
