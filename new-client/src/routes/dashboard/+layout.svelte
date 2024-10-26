<script lang="ts">
  import { goto } from '$app/navigation';
  import { onMount } from 'svelte';
  import { sessionToken } from '../../stores';
  import { removeTokenInMemory } from '$lib/memory';

  const logoutHandler = () => {
    removeTokenInMemory();
    sessionToken.set('');
    goto('/');
  };

  onMount(() => {
    if (!$sessionToken) {
      goto('/login');
    }
  });
</script>

<div class="dashboard">
  <nav class="navigation">
    <a class="button navigation__button" href="/dashboard/new-cs">NEW CHEAT SHEET</a>
    <a class="button navigation__button" href="/dashboard">ALL CHEAT SHEETS</a>
    <button class="button navigation__button" on:click={logoutHandler}>LOGOUT</button>
  </nav>
  <slot />
</div>

<style lang="scss">
  .dashboard {
    display: flex;
    flex-direction: column;
    width: calc(100% - 10px);
    padding: 10px;
  }

  .navigation {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    width: auto;
    margin: 10px;

    &__button {
      margin: 10px;
    }
  }
</style>
