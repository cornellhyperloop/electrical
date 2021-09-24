"use strict";

var _interopRequireWildcard = require("@babel/runtime/helpers/interopRequireWildcard");

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.postKeyupBehavior = exports.keyupBehavior = exports.preKeyupBehavior = exports.keypressBehavior = exports.keydownBehavior = exports.preKeydownBehavior = exports.replaceBehavior = void 0;

var _utils = require("../../utils");

var arrowKeys = _interopRequireWildcard(require("./arrow"));

var controlKeys = _interopRequireWildcard(require("./control"));

var characterKeys = _interopRequireWildcard(require("./character"));

var functionalKeys = _interopRequireWildcard(require("./functional"));

const replaceBehavior = [{
  matches: (keyDef, element) => keyDef.key === 'selectall' && (0, _utils.isElementType)(element, ['input', 'textarea']),
  handle: (keyDef, element, options, state) => {
    var _state$carryValue;

    (0, _utils.setSelectionRange)(element, 0, ((_state$carryValue = state.carryValue) != null ? _state$carryValue : element.value).length);
  }
}];
exports.replaceBehavior = replaceBehavior;
const preKeydownBehavior = [...functionalKeys.preKeydownBehavior];
exports.preKeydownBehavior = preKeydownBehavior;
const keydownBehavior = [...arrowKeys.keydownBehavior, ...controlKeys.keydownBehavior, ...functionalKeys.keydownBehavior];
exports.keydownBehavior = keydownBehavior;
const keypressBehavior = [...functionalKeys.keypressBehavior, ...characterKeys.keypressBehavior];
exports.keypressBehavior = keypressBehavior;
const preKeyupBehavior = [...functionalKeys.preKeyupBehavior];
exports.preKeyupBehavior = preKeyupBehavior;
const keyupBehavior = [...functionalKeys.keyupBehavior];
exports.keyupBehavior = keyupBehavior;
const postKeyupBehavior = [...functionalKeys.postKeyupBehavior];
exports.postKeyupBehavior = postKeyupBehavior;