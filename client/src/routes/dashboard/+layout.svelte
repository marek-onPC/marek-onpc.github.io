<script lang="ts">
  import { goto } from '$app/navigation';
  import { onDestroy, onMount } from 'svelte';
  import { sessionToken } from '../../stores';
  import { removeTokenInMemory, setTokenInMemory } from '$lib/memory';
  import Loader from '../../components/Loader.svelte';
  import { fetchClientPost, fetchClientPostWithoutToken } from '$lib/fetchClient';
  import Modal from '../../components/Modal.svelte';
  import { AuthGrantType, type AuthToken, type AuthTokenResponse } from '../../types';

  let isLoadingNewCheatSheet: boolean = false;
  let isError: boolean = false;
  let hasTokenExpired: boolean = false;
  let checkTokenValidityInterval: number;

  const createNewCheatSheet = async () => {
    try {
      isLoadingNewCheatSheet = true;
      isError = false;

      const newCheatSheetID = await fetchClientPost('/cheat_sheets', $sessionToken.accessToken, {
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

  const refreshTokenLogin = async () => {
    const currentRefreshToken = $sessionToken.refreshToken;

    try {
      const response = await fetchClientPostWithoutToken('/login', {
        grant_type: AuthGrantType.REFRESH_TOKEN,
        refresh_token: currentRefreshToken
      });
      const data = response.data as AuthTokenResponse;

      const expiry = new Date(Date.now() + data.expires_in * 1000); // Convert seconds to milliseconds

      const loginToken: AuthToken = {
        accessToken: data.access_token,
        tokenType: data.token_type,
        expiry: expiry,
        refreshToken: data.refresh_token
      };

      setTokenInMemory(loginToken);
      sessionToken.set(loginToken);
      hasTokenExpired = false;
    } catch (error) {
      logoutHandler();
    }
  };

  const logoutHandler = () => {
    removeTokenInMemory();
    sessionToken.set({ accessToken: '', refreshToken: '', expiry: new Date(), tokenType: '' });
    goto('/login');
  };

  onMount(() => {
    if (!$sessionToken.accessToken || $sessionToken.expiry < new Date()) {
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
      refreshTokenLogin();
    }, 1500);
</script>

<div class="dashboard">
  {#if !$sessionToken.accessToken || $sessionToken.expiry < new Date()}
    <Loader />
  {:else}
    {#if hasTokenExpired}
      <Modal isOpened={hasTokenExpired} text="Token expired, reauthenticating" hasLoader={true} />
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
  {/if}
</div>

<style lang="scss">
  .dashboard {
    display: flex;
    flex-direction: column;
    width: calc(100% - 10px);
    max-width: 1440px;
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
