"use strict";

var _interopRequireDefault = require("@babel/runtime/helpers/interopRequireDefault");

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports["default"] = void 0;

var _regenerator = _interopRequireDefault(require("@babel/runtime/regenerator"));

var _asyncToGenerator2 = _interopRequireDefault(require("@babel/runtime/helpers/asyncToGenerator"));

var _chokidar = _interopRequireDefault(require("chokidar"));

var _fs = _interopRequireDefault(require("fs"));

var _net = require("net");

var _util = require("util");

var openAsync = (0, _util.promisify)(_fs["default"].open);
var readAsync = (0, _util.promisify)(_fs["default"].read);
var statAsync = (0, _util.promisify)(_fs["default"].stat);
var fds = {};
/**
 * Reads new lines from file on disk and sends them to the server
 */

function sendNewMessages(_x, _x2, _x3, _x4, _x5, _x6) {
  return _sendNewMessages.apply(this, arguments);
}
/**
 * Sends an input registration to server
 */


function _sendNewMessages() {
  _sendNewMessages = (0, _asyncToGenerator2["default"])( /*#__PURE__*/_regenerator["default"].mark(function _callee(client, streamName, sourceName, filePath, newSize, oldSize) {
    var fd, offset, readBuffer, messages;
    return _regenerator["default"].wrap(function _callee$(_context) {
      while (1) {
        switch (_context.prev = _context.next) {
          case 0:
            fd = fds[filePath];

            if (fd) {
              _context.next = 6;
              break;
            }

            _context.next = 4;
            return openAsync(filePath, 'r');

          case 4:
            fd = _context.sent;
            fds[filePath] = fd;

          case 6:
            offset = Math.max(newSize - oldSize, 0);
            readBuffer = Buffer.alloc(offset);
            _context.next = 10;
            return readAsync(fd, readBuffer, 0, offset, oldSize);

          case 10:
            messages = readBuffer.toString().split('\r\n').filter(function (msg) {
              return !!msg.trim();
            });
            messages.forEach(function (message) {
              client.write("+msg|".concat(streamName, "|").concat(sourceName, "|").concat(message, "\0"));
            });

          case 12:
          case "end":
            return _context.stop();
        }
      }
    }, _callee);
  }));
  return _sendNewMessages.apply(this, arguments);
}

function sendInput(_x7, _x8) {
  return _sendInput.apply(this, arguments);
}
/**
 * Initializes file watcher for the provided path
 */


function _sendInput() {
  _sendInput = (0, _asyncToGenerator2["default"])( /*#__PURE__*/_regenerator["default"].mark(function _callee2(client, input) {
    return _regenerator["default"].wrap(function _callee2$(_context2) {
      while (1) {
        switch (_context2.prev = _context2.next) {
          case 0:
            client.write("+input|".concat(input.stream, "|").concat(input.source, "\0"));

          case 1:
          case "end":
            return _context2.stop();
        }
      }
    }, _callee2);
  }));
  return _sendInput.apply(this, arguments);
}

function startFileWatcher(_x9, _x10, _x11, _x12, _x13) {
  return _startFileWatcher.apply(this, arguments);
}
/**
 * Async sleep helper
 */
function slp(time = 0) {
	return new Promise((resolve, reject) => {
		setTimeout(() => { resolve(); }, time);
	});
}

function _startFileWatcher() {
  _startFileWatcher = (0, _asyncToGenerator2["default"])( /*#__PURE__*/_regenerator["default"].mark(function _callee5(client, streamName, sourceName, inputPath, watcherOptions) {
    var fileSizes, watcher;
    return _regenerator["default"].wrap(function _callee5$(_context5) {
      while (1) {
        switch (_context5.prev = _context5.next) {
          case 0:
            fileSizes = {};
            watcher = _chokidar["default"].watch(inputPath, watcherOptions); // Capture byte size of a new file

            watcher.on('add', /*#__PURE__*/function () {
              var _ref = (0, _asyncToGenerator2["default"])( /*#__PURE__*/_regenerator["default"].mark(function _callee3(filePath) {
                return _regenerator["default"].wrap(function _callee3$(_context3) {
                  while (1) {
                    switch (_context3.prev = _context3.next) {
                      case 0:
                        // eslint-disable-next-line no-console
                        console.log("[".concat(streamName, "][").concat(sourceName, "] Watching: ").concat(filePath));
                        _context3.next = 3;
                        return statAsync(filePath);

                      case 3:
                        fileSizes[filePath] = _context3.sent.size;

                      case 4:
                      case "end":
                        return _context3.stop();
                    }
                  }
                }, _callee3);
              }));

              return function (_x16) {
                return _ref.apply(this, arguments);
              };
            }()); // Send new lines when a file is changed

            watcher.on('change', /*#__PURE__*/function () {
              var _ref2 = (0, _asyncToGenerator2["default"])( /*#__PURE__*/_regenerator["default"].mark(function _callee4(filePath) {
                var newSize;
                return _regenerator["default"].wrap(function _callee4$(_context4) {
                  while (1) {
                    switch (_context4.prev = _context4.next) {
                      case 0:
                        _context4.prev = 0;
                        _context4.next = 3;
                        return (async () => {
			  await (() => {
			    return new Promise((resolve, reject) => {
		              setTimeout(() => { resolve(); }, 100);
			    });
			  })();
			  return statAsync(filePath);
			})();

                      case 3:
                        newSize = _context4.sent.size;
                        _context4.next = 6;
                        return sendNewMessages(client, streamName, sourceName, filePath, newSize, fileSizes[filePath]);

                      case 6:
                        fileSizes[filePath] = newSize;
                        _context4.next = 12;
                        break;

                      case 9:
                        _context4.prev = 9;
                        _context4.t0 = _context4["catch"](0);
                        // eslint-disable-next-line no-console
                        console.error(_context4.t0);

                      case 12:
                      case "end":
                        return _context4.stop();
                    }
                  }
                }, _callee4, null, [[0, 9]]);
              }));

              return function (_x17) {
                return _ref2.apply(this, arguments);
              };
            }()); // If a file is removed (or moved), delete its file descriptor & size

            watcher.on('unlink', function (filePath) {
              delete fileSizes[filePath];
              delete fds[filePath];
            });

          case 5:
          case "end":
            return _context5.stop();
        }
      }
    }, _callee5);
  }));
  return _startFileWatcher.apply(this, arguments);
}

function sleep(_x14) {
  return _sleep.apply(this, arguments);
}
/**
 * Start file input process
 */


function _sleep() {
  _sleep = (0, _asyncToGenerator2["default"])( /*#__PURE__*/_regenerator["default"].mark(function _callee6(ms) {
    return _regenerator["default"].wrap(function _callee6$(_context6) {
      while (1) {
        switch (_context6.prev = _context6.next) {
          case 0:
            return _context6.abrupt("return", new Promise(function (r) {
              return setTimeout(r, ms);
            }));

          case 1:
          case "end":
            return _context6.stop();
        }
      }
    }, _callee6);
  }));
  return _sleep.apply(this, arguments);
}

function main(_x15) {
  return _main.apply(this, arguments);
}

function _main() {
  _main = (0, _asyncToGenerator2["default"])( /*#__PURE__*/_regenerator["default"].mark(function _callee11(config) {
    var messageServer, inputs, serverStr, client, lastConnectionAttempt;
    return _regenerator["default"].wrap(function _callee11$(_context11) {
      while (1) {
        switch (_context11.prev = _context11.next) {
          case 0:
            messageServer = config.messageServer, inputs = config.inputs;
            serverStr = "".concat(messageServer.host, ":").concat(messageServer.port);
            client = new _net.Socket();
            lastConnectionAttempt = new Date().getTime(); // Register new inputs w/ server

            client.on('connect', /*#__PURE__*/(0, _asyncToGenerator2["default"])( /*#__PURE__*/_regenerator["default"].mark(function _callee8() {
              return _regenerator["default"].wrap(function _callee8$(_context8) {
                while (1) {
                  switch (_context8.prev = _context8.next) {
                    case 0:
                      // eslint-disable-next-line no-console
                      console.log("Connected to server: ".concat(serverStr));
                      _context8.next = 3;
                      return Promise.all(inputs.map( /*#__PURE__*/function () {
                        var _ref4 = (0, _asyncToGenerator2["default"])( /*#__PURE__*/_regenerator["default"].mark(function _callee7(input) {
                          return _regenerator["default"].wrap(function _callee7$(_context7) {
                            while (1) {
                              switch (_context7.prev = _context7.next) {
                                case 0:
                                  sendInput(client, input);

                                case 1:
                                case "end":
                                  return _context7.stop();
                              }
                            }
                          }, _callee7);
                        }));

                        return function (_x18) {
                          return _ref4.apply(this, arguments);
                        };
                      }()));

                    case 3:
                    case "end":
                      return _context8.stop();
                  }
                }
              }, _callee8);
            }))); // Reconnect to server if an error occurs while sending a message

            client.on('error', /*#__PURE__*/(0, _asyncToGenerator2["default"])( /*#__PURE__*/_regenerator["default"].mark(function _callee9() {
              var currTime;
              return _regenerator["default"].wrap(function _callee9$(_context9) {
                while (1) {
                  switch (_context9.prev = _context9.next) {
                    case 0:
                      currTime = new Date().getTime();

                      if (!(currTime - lastConnectionAttempt > 5000)) {
                        _context9.next = 7;
                        break;
                      }

                      lastConnectionAttempt = new Date().getTime(); // eslint-disable-next-line no-console

                      console.error("Unable to connect to server (".concat(serverStr, "), retrying..."));
                      _context9.next = 6;
                      return sleep(5000);

                    case 6:
                      client.connect(messageServer.port, messageServer.host);

                    case 7:
                    case "end":
                      return _context9.stop();
                  }
                }
              }, _callee9);
            }))); // Connect to server & start watching files for changes

            client.connect(messageServer.port, messageServer.host);
            _context11.next = 9;
            return Promise.all(inputs.map( /*#__PURE__*/function () {
              var _ref6 = (0, _asyncToGenerator2["default"])( /*#__PURE__*/_regenerator["default"].mark(function _callee10(input) {
                return _regenerator["default"].wrap(function _callee10$(_context10) {
                  while (1) {
                    switch (_context10.prev = _context10.next) {
                      case 0:
                        return _context10.abrupt("return", startFileWatcher(client, input.stream, input.source, input.config.path, input.config.watcherOptions || {}));

                      case 1:
                      case "end":
                        return _context10.stop();
                    }
                  }
                }, _callee10);
              }));

              return function (_x19) {
                return _ref6.apply(this, arguments);
              };
            }()));

          case 9:
          case "end":
            return _context11.stop();
        }
      }
    }, _callee11);
  }));
  return _main.apply(this, arguments);
}

var _default = main;
exports["default"] = _default;
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIi4uL3NyYy9pbnB1dC50cyJdLCJuYW1lcyI6WyJvcGVuQXN5bmMiLCJmcyIsIm9wZW4iLCJyZWFkQXN5bmMiLCJyZWFkIiwic3RhdEFzeW5jIiwic3RhdCIsImZkcyIsInNlbmROZXdNZXNzYWdlcyIsImNsaWVudCIsInN0cmVhbU5hbWUiLCJzb3VyY2VOYW1lIiwiZmlsZVBhdGgiLCJuZXdTaXplIiwib2xkU2l6ZSIsImZkIiwib2Zmc2V0IiwiTWF0aCIsIm1heCIsInJlYWRCdWZmZXIiLCJCdWZmZXIiLCJhbGxvYyIsIm1lc3NhZ2VzIiwidG9TdHJpbmciLCJzcGxpdCIsImZpbHRlciIsIm1zZyIsInRyaW0iLCJmb3JFYWNoIiwibWVzc2FnZSIsIndyaXRlIiwic2VuZElucHV0IiwiaW5wdXQiLCJzdHJlYW0iLCJzb3VyY2UiLCJzdGFydEZpbGVXYXRjaGVyIiwiaW5wdXRQYXRoIiwid2F0Y2hlck9wdGlvbnMiLCJmaWxlU2l6ZXMiLCJ3YXRjaGVyIiwiY2hva2lkYXIiLCJ3YXRjaCIsIm9uIiwiY29uc29sZSIsImxvZyIsInNpemUiLCJlcnJvciIsInNsZWVwIiwibXMiLCJQcm9taXNlIiwiciIsInNldFRpbWVvdXQiLCJtYWluIiwiY29uZmlnIiwibWVzc2FnZVNlcnZlciIsImlucHV0cyIsInNlcnZlclN0ciIsImhvc3QiLCJwb3J0IiwiU29ja2V0IiwibGFzdENvbm5lY3Rpb25BdHRlbXB0IiwiRGF0ZSIsImdldFRpbWUiLCJhbGwiLCJtYXAiLCJjdXJyVGltZSIsImNvbm5lY3QiLCJwYXRoIl0sIm1hcHBpbmdzIjoiOzs7Ozs7Ozs7Ozs7O0FBQUE7O0FBQ0E7O0FBQ0E7O0FBQ0E7O0FBUUEsSUFBTUEsU0FBUyxHQUFHLHFCQUFVQyxlQUFHQyxJQUFiLENBQWxCO0FBQ0EsSUFBTUMsU0FBUyxHQUFHLHFCQUFVRixlQUFHRyxJQUFiLENBQWxCO0FBQ0EsSUFBTUMsU0FBUyxHQUFHLHFCQUFVSixlQUFHSyxJQUFiLENBQWxCO0FBRUEsSUFBTUMsR0FB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QTdCLEVBQW1DSixhQUFhLENBQUNHLElBQWpEOztBQVBlO0FBQUE7QUFBQTtBQUFBO0FBQUE7QUFBQTtBQUFBLGFBQW5CLElBZEYsQ0F3QkU7O0FBQ0FoRCxZQUFBQSxNQUFNLENBQUN5RCxPQUFQLENBQWVaLGFBQWEsQ0FBQ0ksSUFBN0IsRUFBbUNKLGFBQWEsQ0FBQ0csSUFBakQ7QUF6QkY7QUFBQSxtQkEwQlFSLE9BQU8sQ0FBQ2MsR0FBUixDQUFZUixNQUFNLENBQUNTLEdBQVA7QUFBQSx3R0FBVyxtQkFBT2hDLEtBQVA7QUFBQTtBQUFBO0FBQUE7QUFBQTtBQUFBLDJEQUMzQkcsZ0JBQWdCLENBQ2QxQixNQURjLEVBRWR1QixLQUFLLENBQUNDLE1BRlEsRUFHZEQsS0FBSyxDQUFDRSxNQUhRLEVBSWRGLEtBQUssQ0FBQ3FCLE1BQU4sQ0FBYWMsSUFKQyxFQUtkbkMsS0FBSyxDQUFDcUIsTUFBTixDQUFhaEIsY0FBYixJQUErQixFQUxqQixDQURXOztBQUFBO0FBQUE7QUFBQTtBQUFBO0FBQUE7QUFBQTtBQUFBLGVBQVg7O0FBQUE7QUFBQTtBQUFBO0FBQUEsZ0JBQVosQ0ExQlI7O0FBQUE7QUFBQTtBQUFBO0FBQUE7QUFBQTtBQUFBO0FBQUEsRzs7OztlQXFDZWUsSSIsInNvdXJjZXNDb250ZW50IjpbImltcG9ydCBjaG9raWRhciBmcm9tICdjaG9raWRhcidcbmltcG9ydCBmcyBmcm9tICdmcydcbmltcG9ydCB7IFNvY2tldCB9IGZyb20gJ25ldCdcbmltcG9ydCB7IHByb21pc2lmeSB9IGZyb20gJ3V0aWwnXG5pbXBvcnQge1xuICBGaWxlSW5wdXRDb25maWcsXG4gIEZpbGVTaXplTWFwLFxuICBJbnB1dENvbmZpZyxcbiAgV2F0Y2hlck9wdGlvbnMsXG59IGZyb20gJy4vdHlwZXMnXG5cbmNvbnN0IG9wZW5Bc3luYyA9IHByb21pc2lmeShmcy5vcGVuKVxuY29uc3QgcmVhZEFzeW5jID0gcHJvbWlzaWZ5KGZzLnJlYWQpXG5jb25zdCBzdGF0QXN5bmMgPSBwcm9taXNpZnkoZnMuc3RhdClcblxuY29uc3QgZmRzOiB7W2ZpbGVQYXRoOiBzdHJpbmddOiBudW1iZXJ9ID0ge31cblxuLyoqXG4gKiBSZWFkcyBuZXcgbGluZXMgZnJvbSBmaWxlIG9uIGRpc2sgYW5kIHNlbmRzIHRoZW0gdG8gdGhlIHNlcnZlclxuICovXG5hc3luYyBmdW5jdGlvbiBzZW5kTmV3TWVzc2FnZXMoXG4gIGNsaWVudDogU29ja2V0LFxuICBzdHJlYW1OYW1lOiBzdHJpbmcsXG4gIHNvdXJjZU5hbWU6IHN0cmluZyxcbiAgZmlsZVBhdGg6IHN0cmluZyxcbiAgbmV3U2l6ZTogbnVtYmVyLFxuICBvbGRTaXplOiBudW1iZXIsXG4pOiBQcm9taXNlPHZvaWQ+IHtcbiAgbGV0IGZkID0gZmRzW2ZpbGVQYXRoXVxuICBpZiAoIWZkKSB7XG4gICAgZmQgPSBhd2FpdCBvcGVuQXN5bmMoZmlsZVBhdGgsICdyJylcbiAgICBmZHNbZmlsZVBhdGhdID0gZmRcbiAgfVxuICBjb25zdCBvZmZzZXQgPSBNYXRoLm1heChuZXdTaXplIC0gb2xkU2l6ZSwgMClcbiAgY29uc3QgcmVhZEJ1ZmZlciA9IEJ1ZmZlci5hbGxvYyhvZmZzZXQpXG4gIGF3YWl0IHJlYWRBc3luYyhmZCwgcmVhZEJ1ZmZlciwgMCwgb2Zmc2V0LCBvbGRTaXplKVxuICBjb25zdCBtZXNzYWdlcyA9IHJlYWRCdWZmZXIudG9TdHJpbmcoKS5zcGxpdCgnXFxyXFxuJykuZmlsdGVyKChtc2cpID0+ICEhbXNnLnRyaW0oKSlcbiAgbWVzc2FnZXMuZm9yRWFjaCgobWVzc2FnZSkgPT4ge1xuICAgIGNsaWVudC53cml0ZShgK21zZ3wke3N0cmVhbU5hbWV9fCR7c291cmNlTmFtZX18JHttZXNzYWdlfVxcMGApXG4gIH0pXG59XG5cbi8qKlxuICogU2VuZHMgYW4gaW5wdXQgcmVnaXN0cmF0aW9uIHRvIHNlcnZlclxuICovXG5hc3luYyBmdW5jdGlvbiBzZW5kSW5wdXQoXG4gIGNsaWVudDogU29ja2V0LFxuICBpbnB1dDogRmlsZUlucHV0Q29uZmlnLFxuKTogUHJvbWlzZTx2b2lkPiB7XG4gIGNsaWVudC53cml0ZShgK2lucHV0fCR7aW5wdXQuc3RyZWFtfXwke2lucHV0LnNvdXJjZX1cXDBgKVxufVxuXG4vKipcbiAqIEluaXRpYWxpemVzIGZpbGUgd2F0Y2hlciBmb3IgdGhlIHByb3ZpZGVkIHBhdGhcbiAqL1xuYXN5bmMgZnVuY3Rpb24gc3RhcnRGaWxlV2F0Y2hlcihcbiAgY2xpZW50OiBTb2NrZXQsXG4gIHN0cmVhbU5hbWU6IHN0cmluZyxcbiAgc291cmNlTmFtZTogc3RyaW5nLFxuICBpbnB1dFBhdGg6IHN0cmluZyxcbiAgd2F0Y2hlck9wdGlvbnM6IFdhdGNoZXJPcHRpb25zLFxuKTogUHJvbWlzZTx2b2lkPiB7XG4gIGNvbnN0IGZpbGVTaXplczogRmlsZVNpemVNYXAgPSB7fVxuICBjb25zdCB3YXRjaGVyID0gY2hva2lkYXIud2F0Y2goaW5wdXRQYXRoLCB3YXRjaGVyT3B0aW9ucylcbiAgLy8gQ2FwdHVyZSBieXRlIHNpemUgb2YgYSBuZXcgZmlsZVxuICB3YXRjaGVyLm9uKCdhZGQnLCBhc3luYyAoZmlsZVBhdGg6IHN0cmluZykgPT4ge1xuICAgIC8vIGVzbGludC1kaXNhYmxlLW5leHQtbGluZSBuby1jb25zb2xlXG4gICAgY29uc29sZS5sb2coYFske3N0cmVhbU5hbWV9XVske3NvdXJjZU5hbWV9XSBXYXRjaGluZzogJHtmaWxlUGF0aH1gKVxuICAgIGZpbGVTaXplc1tmaWxlUGF0aF0gPSAoYXdhaXQgc3RhdEFzeW5jKGZpbGVQYXRoKSkuc2l6ZVxuICB9KVxuICAvLyBTZW5kIG5ldyBsaW5lcyB3aGVuIGEgZmlsZSBpcyBjaGFuZ2VkXG4gIHdhdGNoZXIub24oJ2NoYW5nZScsIGFzeW5jIChmaWxlUGF0aDogc3RyaW5nKSA9PiB7XG4gICAgdHJ5IHtcbiAgICAgIGNvbnN0IG5ld1NpemUgPSAoYXdhaXQgc3RhdEFzeW5jKGZpbGVQYXRoKSkuc2l6ZVxuICAgICAgYXdhaXQgc2VuZE5ld01lc3NhZ2VzKFxuICAgICAgICBjbGllbnQsXG4gICAgICAgIHN0cmVhbU5hbWUsXG4gICAgICAgIHNvdXJjZU5hbWUsXG4gICAgICAgIGZpbGVQYXRoLFxuICAgICAgICBuZXdTaXplLFxuICAgICAgICBmaWxlU2l6ZXNbZmlsZVBhdGhdLFxuICAgICAgKVxuICAgICAgZmlsZVNpemVzW2ZpbGVQYXRoXSA9IG5ld1NpemVcbiAgICB9IGNhdGNoIChlcnIpIHtcbiAgICAgIC8vIGVzbGludC1kaXNhYmxlLW5leHQtbGluZSBuby1jb25zb2xlXG4gICAgICBjb25zb2xlLmVycm9yKGVycilcbiAgICB9XG4gIH0pXG4gIC8vIElmIGEgZmlsZSBpcyByZW1vdmVkIChvciBtb3ZlZCksIGRlbGV0ZSBpdHMgZmlsZSBkZXNjcmlwdG9yICYgc2l6ZVxuICB3YXRjaGVyLm9uKCd1bmxpbmsnLCAoZmlsZVBhdGg6IHN0cmluZykgPT4ge1xuICAgIGRlbGV0ZSBmaWxlU2l6ZXNbZmlsZVBhdGhdXG4gICAgZGVsZXRlIGZkc1tmaWxlUGF0aF1cbiAgfSlcbn1cblxuLyoqXG4gKiBBc3luYyBzbGVlcCBoZWxwZXJcbiAqL1xuYXN5bmMgZnVuY3Rpb24gc2xlZXAobXM6IG51bWJlcik6IFByb21pc2U8dm9pZD4ge1xuICByZXR1cm4gbmV3IFByb21pc2UoKHIpID0+IHNldFRpbWVvdXQociwgbXMpKVxufVxuXG4vKipcbiAqIFN0YXJ0IGZpbGUgaW5wdXQgcHJvY2Vzc1xuICovXG5hc3luYyBmdW5jdGlvbiBtYWluKGNvbmZpZzogSW5wdXRDb25maWcpOiBQcm9taXNlPHZvaWQ+IHtcbiAgY29uc3QgeyBtZXNzYWdlU2VydmVyLCBpbnB1dHMgfSA9IGNvbmZpZ1xuICBjb25zdCBzZXJ2ZXJTdHIgPSBgJHttZXNzYWdlU2VydmVyLmhvc3R9OiR7bWVzc2FnZVNlcnZlci5wb3J0fWBcbiAgY29uc3QgY2xpZW50ID0gbmV3IFNvY2tldCgpXG4gIGxldCBsYXN0Q29ubmVjdGlvbkF0dGVtcHQgPSBuZXcgRGF0ZSgpLmdldFRpbWUoKVxuICAvLyBSZWdpc3RlciBuZXcgaW5wdXRzIHcvIHNlcnZlclxuICBjbGllbnQub24oJ2Nvbm5lY3QnLCBhc3luYyAoKSA9PiB7XG4gICAgLy8gZXNsaW50LWRpc2FibGUtbmV4dC1saW5lIG5vLWNvbnNvbGVcbiAgICBjb25zb2xlLmxvZyhgQ29ubmVjdGVkIHRvIHNlcnZlcjogJHtzZXJ2ZXJTdHJ9YClcbiAgICBhd2FpdCBQcm9taXNlLmFsbChpbnB1dHMubWFwKGFzeW5jIChpbnB1dCkgPT4ge1xuICAgICAgc2VuZElucHV0KGNsaWVudCwgaW5wdXQpXG4gICAgfSkpXG4gIH0pXG4gIC8vIFJlY29ubmVjdCB0byBzZXJ2ZXIgaWYgYW4gZXJyb3Igb2NjdXJzIHdoaWxlIHNlbmRpbmcgYSBtZXNzYWdlXG4gIGNsaWVudC5vbignZXJyb3InLCBhc3luYyAoKSA9PiB7XG4gICAgY29uc3QgY3VyclRpbWUgPSBuZXcgRGF0ZSgpLmdldFRpbWUoKVxuICAgIGlmIChjdXJyVGltZSAtIGxhc3RDb25uZWN0aW9uQXR0ZW1wdCA+IDUwMDApIHtcbiAgICAgIGxhc3RDb25uZWN0aW9uQXR0ZW1wdCA9IG5ldyBEYXRlKCkuZ2V0VGltZSgpXG4gICAgICAvLyBlc2xpbnQtZGlzYWJsZS1uZXh0LWxpbmUgbm8tY29uc29sZVxuICAgICAgY29uc29sZS5lcnJvcihgVW5hYmxlIHRvIGNvbm5lY3QgdG8gc2VydmVyICgke3NlcnZlclN0cn0pLCByZXRyeWluZy4uLmApXG4gICAgICBhd2FpdCBzbGVlcCg1MDAwKVxuICAgICAgY2xpZW50LmNvbm5lY3QobWVzc2FnZVNlcnZlci5wb3J0LCBtZXNzYWdlU2VydmVyLmhvc3QpXG4gICAgfVxuICB9KVxuICAvLyBDb25uZWN0IHRvIHNlcnZlciAmIHN0YXJ0IHdhdGNoaW5nIGZpbGVzIGZvciBjaGFuZ2VzXG4gIGNsaWVudC5jb25uZWN0KG1lc3NhZ2VTZXJ2ZXIucG9ydCwgbWVzc2FnZVNlcnZlci5ob3N0KVxuICBhd2FpdCBQcm9taXNlLmFsbChpbnB1dHMubWFwKGFzeW5jIChpbnB1dCkgPT4gKFxuICAgIHN0YXJ0RmlsZVdhdGNoZXIoXG4gICAgICBjbGllbnQsXG4gICAgICBpbnB1dC5zdHJlYW0sXG4gICAgICBpbnB1dC5zb3VyY2UsXG4gICAgICBpbnB1dC5jb25maWcucGF0aCxcbiAgICAgIGlucHV0LmNvbmZpZy53YXRjaGVyT3B0aW9ucyB8fCB7fSxcbiAgICApXG4gICkpKVxufVxuXG5leHBvcnQgZGVmYXVsdCBtYWluXG4iXX0=
