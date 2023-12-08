import {
    composeNextState,
} from '@openfn/language-common';
import axios from 'axios';

/**
 * Fetch the list of outbreaks
 * @public
 * @example
 *  listOutbreaks(state => {
 *    console.log(state.data);
 *    return state;
 *  });
 * @function
 * @param {function} callback - (Optional) Callback function
 * @returns {Operation}
 */
export function listOutbreaks(callback) {
    return state => {
        const { apiUrl, access_token } = state.configuration;

        return axios({
            method: 'GET',
            baseURL: apiUrl,
            url: '/outbreaks',
            params: {
                access_token,
            },
        })
            .then(response => {
                const nextState = composeNextState(state, response.data);
                if (callback) return callback(nextState);
                return nextState;
            })
            .catch(error => {
                return error;
            });
    };
}