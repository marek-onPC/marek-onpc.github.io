<script lang="ts">
  import { fetchClientPostWithoutToken } from '$lib/fetchClient';
  import type { AuthCredentials } from '../../types';
  import { sessionToken } from '../../stores';
  import { getTokenFromMemory, setTokenInMemory } from '$lib/memory';
  import { onMount } from 'svelte';
  import { goto } from '$app/navigation';
  import Loader from '../../components/Loader.svelte';

  let user: AuthCredentials = {
    username: '',
    password: ''
  };
  let isUsernameFocused: boolean = false;
  let isPasswordFocused: boolean = false;
  let isLoginInProgress: boolean = false;
  let isLoginError: boolean = false;

  const loginHandler = async () => {
    isLoginInProgress = true;
    isLoginError = false;

    try {
      const response = await fetchClientPostWithoutToken('/login', user);

      setTokenInMemory(response.data.token);
      sessionToken.set(response.data.token);

      setTimeout(() => {
        goto('/dashboard');
      }, 500);
    } catch (error) {
      isLoginInProgress = false;
      isLoginError = true;
    }
  };

  onMount(() => {
    const currentToken = getTokenFromMemory();

    if (currentToken) {
      goto('/dashboard');
    }
  });
</script>

<div class="login">
  <form class="login__form">
    <div class="login__input {isUsernameFocused ? '--focused' : ''}">
      <input
        name="username"
        placeholder="Username"
        class="input"
        disabled={isLoginInProgress}
        bind:value={user.username}
        on:focusin={() => (isUsernameFocused = true)}
        on:focusout={() => (isUsernameFocused = false)}
      />
    </div>
    <div class="login__input {isPasswordFocused ? '--focused' : ''}">
      <input
        name="password"
        placeholder="Password"
        type="password"
        class="input"
        disabled={isLoginInProgress}
        bind:value={user.password}
        on:focusin={() => (isPasswordFocused = true)}
        on:focusout={() => (isPasswordFocused = false)}
      />
    </div>
  </form>

  <button class="button login__submit" on:click={loginHandler} disabled={isLoginInProgress}>
    {#if isLoginInProgress}
      <Loader isSmall={true} isWhite={true} />
    {:else}
      Create new
    {/if}
  </button>

  {#if isLoginError}
    <div class="login__error">
      <p>Error occurred on login, try again.</p>
    </div>
  {:else}
    <div class="login__spacer"></div>
  {/if}
</div>

<style lang="scss">
  .login {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100%;
    min-height: calc(100vh - 10px);

    &__form {
      display: flex;
    }

    &__input {
      position: relative;
      margin: 20px;

      &::after {
        position: absolute;
        bottom: 0px;
        left: 0px;
        content: '';
        display: block;
        width: 0%;
        height: 3px;
        background-color: #42b883;
        transition: 0.15s ease-in-out;
      }

      ::placeholder {
        transition: 0.15s ease-in-out;
      }

      &.--focused {
        &::after {
          width: 100%;
        }

        ::placeholder {
          opacity: 0.5;
        }
      }
    }

    &__submit {
      height: 50px;
    }

    &__error {
      border-radius: 5px;
      margin-top: 50px;
      padding: 0px 20px;
      background-color: rgb(253, 237, 237);

      p {
        color: rgb(95, 33, 32);
        font-size: 14px;
      }
    }

    &__spacer {
      display: block;
      background-color: transparent;
      height: 96.5px;
    }
  }
</style>
