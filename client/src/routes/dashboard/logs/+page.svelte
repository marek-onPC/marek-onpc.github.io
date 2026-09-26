<script lang="ts">
  import { onMount, tick } from 'svelte';
  import { sessionToken } from '../../../stores';
  import { fetchClientGet } from '$lib/fetchClient';
  import type { LogEntry } from '../../../types';
  import Loader from '../../../components/Loader.svelte';

  const PAGE_SIZE = 20;

  let logsData: LogEntry[] = [];
  let listEl: HTMLDivElement;
  let isInitialLoad = true;
  let isLoadingMore = false;
  let hasMore = true;
  let offset = 0;

  const loadLogs = async (skip: number, limit: number): Promise<LogEntry[]> => {
    const raw = await fetchClientGet(
      '/logs',
      $sessionToken.accessToken,
      {},
      { skip, limit }
    );
    return (raw.data as LogEntry[] | null) ?? [];
  };

  const loadMoreLogs = async (): Promise<void> => {
    if (isLoadingMore || !hasMore)
    {
      return;
    }
  
    try {
      isLoadingMore = true;

      const loadedLogs = await loadLogs(offset, PAGE_SIZE);

      logsData = [...logsData, ...loadedLogs];
      offset += PAGE_SIZE;
      hasMore = false ? loadedLogs.length < PAGE_SIZE : true;

      await tick();
      if (listEl) {
        listEl.scrollTop = listEl.scrollHeight - listEl.clientHeight;
      }
    } catch (e) {
      console.error(e);
    } finally {
      isLoadingMore = false;
    }
  };

  const initialLoad = async (): Promise<void> => {
    try {
      const loadedLogs = await loadLogs(0, PAGE_SIZE);

      logsData = loadedLogs;
      offset = PAGE_SIZE;
      hasMore = loadedLogs.length >= PAGE_SIZE;
    } catch (e) {
      console.error(e);
    } finally {
      isInitialLoad = false;
    }
  };

  onMount(() => {
    initialLoad();
  });
</script>

<div class="logs-page">
  {#if isInitialLoad}
    <Loader />
  {:else}
    <div class="logs-page__list" bind:this={listEl}>
      {#each logsData as log (log.id)}
        <p class="logs-page__line"><strong>[{new Date(log.timestamp).toLocaleString()}]</strong> ({log.user ? log.user : ''}) {log.event_type}: {log.message}</p>
      {/each}
    </div>
    {#if hasMore}
      <button
        class="button logs-page__load-more"
        on:click={loadMoreLogs}
        disabled={isLoadingMore}
      >
        {#if isLoadingMore}
          <Loader isSmall={true} isWhite={true} />
        {:else}
          Load more
        {/if}
      </button>
    {/if}
  {/if}
</div>

<style lang="scss">
  .logs-page {
    padding: 1rem;
    max-width: 1440px;

    &__list {
      width: 100%;
      background-color: #fff;
      border: 2px solid #fff;
      border-radius: 5px;
      padding: 15px;
      margin-top: 1rem;
      box-sizing: border-box;
      max-height: calc(80vh - 100px);
      overflow-y: auto;
    }

    &__line {
      margin-bottom: 10px;
      margin-bottom: 0.5rem;
      font-size: 14px;
      color: #444;
      font-family: "JetBrains Mono", "Fira Code", "Cascadia Code", Consolas, "Courier New", monospace;
    }

    &__load-more {
      margin: 1rem auto 0;
      min-width: 150px;
    }
  }
</style>
