# Safari

To run Safari on macOS, some manual setup is required:

  * Allow Safari to be controlled by SafariDriver: `safaridriver --enable`

  * Allow pop-up windows:
    `defaults write com.apple.Safari WebKitJavaScriptCanOpenWindowsAutomatically 1`

  * Turn on experimental features that are "off" by default:

    * `defaults write com.apple.Safari ExperimentalServerTimingEnabled -bool true`

    [//]: # (TODO\(cvazac\) Remove this if/when Server-Timing is enabled by default in Safari)

  * Trust the certificate:
    `security add-trusted-cert -k "$(security default-keychain | cut -d\" -f2)" tools/certs/cacert.pem`

  * Set `no_proxy='*'` in your environment. This is a
    workaround for a known
    [macOS High Sierra issue](https://github.com/web-platform-tests/wpt/issues/9007).

Now, run the tests using the `safari` product:
```
./wpt run safari [test_list]
```

This will use the `safaridriver` found on the path, which will be stable Safari.
To run Safari Technology Preview instead, use the `--channel=preview` argument:
```
./wpt run --channel=preview safari [test_list]
```
