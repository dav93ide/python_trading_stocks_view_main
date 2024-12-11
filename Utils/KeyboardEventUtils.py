from pyglet.window import key
from Utils.NumberUtils import NumberUtils

ENTRY_ID = "id"
ENTRY_KEY_EVENT = "keyEvent"
ENTRY_SELECTION_EVENT = "selectionEvent"

MASK_STARTED_RIGHT_SELECTION = 1
MASK_STARTED_LEFT_SELECTION = -1

class KeyboardEventUtils(object):

    __mLastEvt = {}

    def on_change_text_check_is_int_value(self, evt):
        txt = evt.GetEventObject()
        strng = txt.GetValue()
        rawKey = evt.GetRawKeyCode()
        modifiers = evt.GetModifiers()

        if KeyboardEventUtils.__mLastEvt != None and len(KeyboardEventUtils.__mLastEvt) > 0 and KeyboardEventUtils.__mLastEvt[ENTRY_ID] != txt.GetId():
            self._mLastEvt = {}

        if chr(rawKey).isnumeric() or (rawKey == key.PERIOD and not chr(rawKey) in strng and len(strng) > 0) or (rawKey == key.MINUS and not chr(rawKey) in strng and (len(strng) == 0 or txt.GetInsertionPoint() == 0)):
            pos = txt.GetInsertionPoint()
            txt.SetValue(str(float(txt.GetValue()[:pos] + chr(rawKey) + txt.GetValue()[pos:])))
            txt.SetInsertionPoint(pos + 1)

        elif (modifiers == 4 or modifiers == key.MOD_SHIFT) and rawKey == key.LEFT:             # 4 (?) key.MOD_SHIFT (?)
            pos = txt.GetInsertionPoint()
            rng = list(txt.GetSelection())

            if rng[0] == rng[1] and ENTRY_SELECTION_EVENT in KeyboardEventUtils.__mLastEvt:
                del KeyboardEventUtils.__mLastEvt[ENTRY_SELECTION_EVENT]

            if ENTRY_SELECTION_EVENT in KeyboardEventUtils.__mLastEvt and KeyboardEventUtils.__mLastEvt[ENTRY_SELECTION_EVENT] == MASK_STARTED_RIGHT_SELECTION:

                rng[1] = rng[1] - 1
            else:
                KeyboardEventUtils.__mLastEvt[ENTRY_SELECTION_EVENT] = MASK_STARTED_LEFT_SELECTION
                rng[0] = rng[0] - 1

            txt.SetSelection(rng[0], rng[1])

        elif (modifiers == 4 or modifiers == key.MOD_SHIFT):                                    # 4 (?) key.MOD_SHIFT (?)
            pos = txt.GetInsertionPoint()
            rng = list(txt.GetSelection())

            if rng[0] == rng[1] and ENTRY_SELECTION_EVENT in KeyboardEventUtils.__mLastEvt:
                del KeyboardEventUtils.__mLastEvt[ENTRY_SELECTION_EVENT]

            if ENTRY_SELECTION_EVENT in KeyboardEventUtils.__mLastEvt and KeyboardEventUtils.__mLastEvt[ENTRY_SELECTION_EVENT] == MASK_STARTED_LEFT_SELECTION:
                rng[0] = rng[0] + 1
            else:
                KeyboardEventUtils.__mLastEvt[ENTRY_SELECTION_EVENT] = MASK_STARTED_RIGHT_SELECTION
                rng[1] = rng[1] + 1

            txt.SetSelection(rng[0], rng[1])

        elif rawKey == key.LEFT:
            rng = list(txt.GetSelection())

            if rng[0] != rng[1]:
                txt.SetInsertionPoint(rng[0])
            else:
                txt.SetInsertionPoint(txt.GetInsertionPoint() - 1)

        elif rawKey == key.RIGHT:
            rng = list(txt.GetSelection())

            if rng[0] != rng[1]:
                txt.SetInsertionPoint(rng[1])
            else:
                txt.SetInsertionPoint(txt.GetInsertionPoint() + 1)

        elif rawKey == key.UP or rawKey == key.DOWN:
            pass

        elif rawKey == key.BACKSPACE:                                              
            pos = txt.GetInsertionPoint()
            if txt.GetStringSelection() == "":
                txt.SetValue(txt.GetValue()[:pos-1] + txt.GetValue()[pos:])
                txt.SetInsertionPoint(pos - 0x1)
            else:
                r = txt.GetSelection()
                txt.SetValue(txt.GetValue()[:r[0]] + txt.GetValue()[r[1]:])
                txt.SetInsertionPoint(pos)

        elif rawKey == key.DELETE:
            pos = txt.GetInsertionPoint()
            if txt.GetStringSelection() == "":
                txt.SetValue(txt.GetValue()[:pos] + txt.GetValue()[pos+1:])
            else:
                r = txt.GetSelection()
                txt.SetValue(txt.GetValue()[:r[0]] + txt.GetValue()[r[1]:])
            txt.SetInsertionPoint(pos)

        elif modifiers == key.MOD_CTRL and rawKey == key.A:
            txt.SelectAll()

        else:

            KeyboardEventUtils.__mLastEvt[ENTRY_ID] = txt.GetId()
            KeyboardEventUtils.__mLastEvt[ENTRY_KEY_EVENT] = evt
            return False

        KeyboardEventUtils.__mLastEvt[ENTRY_ID] = txt.GetId()
        KeyboardEventUtils.__mLastEvt[ENTRY_KEY_EVENT] = evt
        return True