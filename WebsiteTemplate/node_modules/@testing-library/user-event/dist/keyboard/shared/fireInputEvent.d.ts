import { fireEvent } from '@testing-library/dom';
export declare function fireInputEvent(element: HTMLElement, { newValue, newSelectionStart, eventOverrides, }: {
    newValue: string;
    newSelectionStart: number;
    eventOverrides: Partial<Parameters<typeof fireEvent>[1]> & {
        [k: string]: unknown;
    };
}): void;
