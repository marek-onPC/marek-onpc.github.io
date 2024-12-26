<script lang="ts">
  import { goto } from '$app/navigation';
  import { onDestroy, onMount } from 'svelte';
  import { sessionToken } from '../../stores';
  import { removeTokenInMemory } from '$lib/memory';
  import Loader from '../../components/Loader.svelte';
  import { fetchClientPost } from '$lib/fetchClient';
  import Modal from '../../components/Modal.svelte';

  let isLoadingNewCheatSheet: boolean = false;
  let isError: boolean = false;
  let hasTokenExpired: boolean = false;
  let checkTokenValidityInterval: number;

  const createNewCheatSheet = async () => {
    try {
      isLoadingNewCheatSheet = true;
      isError = false;

      const newCheatSheetID = await fetchClientPost('/cheat_sheets', $sessionToken.token, {
        title: 'New cheat sheet',
        is_published: false
      });
      goto(`/dashboard/cs-edit/${newCheatSheetID.id}`);
    } catch (error) {
      isLoadingNewCheatSheet = false;
      isError = true;
    }
    isLoadingNewCheatSheet = false;
  };

  const logoutHandler = () => {
    removeTokenInMemory();
    sessionToken.set({ token: '', expiry: new Date() });
    goto('/login');
  };

  onMount(() => {
    if (!$sessionToken.token) {
      goto('/login');
      return;
    }

    checkTokenValidityInterval = setInterval(() => {
      if ($sessionToken.expiry < new Date()) {
        hasTokenExpired = true;
      }
    }, 10000);
  });

  onDestroy(() => clearInterval(checkTokenValidityInterval));

  $: hasTokenExpired &&
    setTimeout(() => {
      logoutHandler();
    }, 1500);
</script>

<div class="dashboard">
  {#if hasTokenExpired}
    <Modal isOpened={hasTokenExpired} text="Token expired, logging out" hasLoader={true} />
  {/if}
  <nav class="navigation">
    <button
      class="button navigation__button"
      on:click={createNewCheatSheet}
      disabled={isLoadingNewCheatSheet}
    >
      {#if isLoadingNewCheatSheet}
        <Loader isSmall={true} isWhite={true} />
      {:else}
        Create new
      {/if}
    </button>
    <a class="button navigation__button" href="/dashboard">All sheets</a>
    <button class="button navigation__button" on:click={logoutHandler}>Logout</button>
  </nav>
  <slot />
</div>

<style lang="scss">
  .dashboard {
    display: flex;
    flex-direction: column;
    width: calc(100% - 10px);
    max-width: 800px;
    padding: 10px;
    margin: 0 auto;
  }

  .navigation {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    width: auto;
    margin: 10px 10px 35px 10px;

    &__button {
      margin: 10px;
    }

    button {
      min-width: 150px;
    }
  }
</style>
