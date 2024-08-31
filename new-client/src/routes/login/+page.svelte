<script lang="ts">
  let username: string = '';
  let password: string = '';
  let isUsernameFocused: boolean = false;
  let isPasswordFocused: boolean = false;

  const loginHandler = () => {
    console.log('username: ' + username);
    console.log('password: ' + password);
  };
</script>

<div class="login">
  <form class="login__form">
    <div class="login__input {isUsernameFocused ? '--focused' : ''}">
      <input
        name="username"
        placeholder="Username"
        class="input"
        bind:value={username}
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
        bind:value={password}
        on:focusin={() => (isPasswordFocused = true)}
        on:focusout={() => (isPasswordFocused = false)}
      />
    </div>
  </form>

  <button class="button login__submit" on:click={loginHandler}>Login</button>
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
  }
</style>
