# Copyright (c) 2021-2022, NVIDIA CORPORATION & AFFILIATES
#
# SPDX-License-Identifier: BSD-3-Clause

import multiprocessing

from .benchmarks.hidden_shift import HiddenShift
from .benchmarks.ghz import GHZ
from .benchmarks.qaoa import QAOA
from .benchmarks.qft import QFT
from .benchmarks.iqft import IQFT
from .benchmarks.qpe import QPE
from .benchmarks.quantum_volume import QuantumVolume
from .benchmarks.random import Random
from .benchmarks.simon import Simon


#########################################################################################################
########################################### Benchmarks Config ###########################################
#########################################################################################################

benchmarks = {

    'qft': {
        'benchmark': QFT,
        'nqubits': {
            'default': list(range(16, 32, 4)) + [30],
            '3090': list(range(16, 32, 4)) + [30],
            'A6000': list(range(16, 32, 4)) + [30],
            'A100-SXM4-80GB': list(range(16, 34, 2)) + [33],
        },
        'config': {
            'measure': True,
        },
    },

    'iqft': {
        'benchmark': IQFT,
        'nqubits': {
            'default': list(range(16, 32, 4)) + [30],
            '3090': list(range(16, 32, 4)) + [30],
            'A6000': list(range(16, 32, 4)) + [30],
            'A100-SXM4-80GB': list(range(16, 34, 2)) + [33],
        },
        'config': {
            'measure': True,
        },
    },

    'ghz': {
        'benchmark': GHZ,
        'nqubits': {
            'default': list(range(16, 32, 4)) + [30],
            '3090': list(range(16, 32, 4)) + [30],
            'A6000': list(range(16, 32, 4)) + [30],
            'A100-SXM4-80GB': list(range(16, 34, 2)) + [33],
        },
        'config': {
            'measure': True,
        },
    },

    'simon': {
        'benchmark': Simon,
        'nqubits': {
            'default': list(range(6, 16, 2)) + [15],
            '3090': list(range(6, 16, 2)) + [15],
            'A6000': list(range(6, 16, 2)) + [15],
            'A100-SXM4-80GB': list(range(6, 17, 1)),
        },
        'config': {
            'measure': True,
        },
    },

    'hidden_shift': {
        'benchmark': HiddenShift,
        'nqubits': {
            'default': list(range(16, 32, 4)) + [30],
            '3090': list(range(16, 32, 4)) + [30],
            'A6000': list(range(16, 32, 4)) + [30],
            'A100-SXM4-80GB': list(range(16, 34, 2)) + [33],
        },
        'config': {
            'measure': True,
        },
    },

    'qaoa': {
        'benchmark': QAOA,
        'nqubits': {
            'default': list(range(16, 32, 4)) + [30],
            '3090': list(range(16, 32, 4)) + [30],
            'A6000': list(range(16, 32, 4)) + [30],
            'A100-SXM4-80GB': list(range(16, 34, 2)) + [33],
        },
        'config': {
            'measure': True,
            'p': 1,
        },
    },

    'qpe': {
        'benchmark': QPE,
        'nqubits': {
            'default': list(range(16, 32, 4)) + [30],
            '3090': list(range(16, 32, 4)) + [30],
            'A6000': list(range(16, 32, 4)) + [30],
            'A100-SXM4-80GB': list(range(16, 34, 2)),
        },
        'config': {
            'measure': True,
            'unfold': False,
        },
    },

    'quantum_volume': {
        'benchmark': QuantumVolume,
        'nqubits': {
            'default': list(range(16, 32, 4)) + [30],
        },
        'config': {
            'measure': True,
        },
    },

    'random': {
        'benchmark': Random,
        'nqubits': {
            'default': list(range(16, 32, 4)) + [30],
            '3090': list(range(16, 32, 4)) + [30],
            'A6000': list(range(16, 32, 4)) + [30],
            'A100-SXM4-80GB': list(range(16, 34, 2)),
        },
        'config': {
            'measure': True,
        },
    },
}

#########################################################################################################
############################################ Backends Config ############################################
#########################################################################################################

backends = {

    'cutn': {
        'config': {
            'nshots': 0,
            'nfused': None,
            'ngpus': 1,
            # TODO: even this may not be a good default
            'ncputhreads': multiprocessing.cpu_count() // 2,
            'precision': 'single',
        },
    },

    'aer': {
        'config': {
            'nshots': 1024,
            'nfused': 5,
            'ngpus': 0,
            'ncputhreads': multiprocessing.cpu_count(),
            'precision':'single',
        },
    },

    'aer-cuda': {
        'config': {
            'nshots': 1024,
            'nfused': 5,
            'ngpus': 1,
            'ncputhreads': multiprocessing.cpu_count(),
            'precision':'single',
        },
    },

    'aer-cusv': {
        'config': {
            'nshots': 1024,
            'nfused': 5,
            'ngpus': 1,
            'ncputhreads': multiprocessing.cpu_count(),
            'precision':'single',
        },
    },

    'cusvaer': {
        'config': {
            'nshots': 1024,
            'nfused': 4,
            'ngpus': 8,
            'ncputhreads': multiprocessing.cpu_count(),
            'precision':'single',
        },
    },

    'cirq': {
        'config': {
            'nshots': 1024,
            'nfused': 4,
            'ngpus': 0,
            'ncputhreads': 1,
            'precision':'single',
        },
    },

    'qsim': {
        'config': {
            'nshots': 1024,
            'nfused': 2,
            'ngpus': 0,
            'ncputhreads': multiprocessing.cpu_count(),
            'precision':'single',
        },
    },

    'qsim-cuda': {
        'config': {
            'nshots': 1024,
            'nfused': 2,
            'ngpus': 1,
            'ncputhreads': 1,
            'precision':'single',
        },
    },

    'qsim-cusv': {
        'config': {
            'nshots': 1024,
            'nfused': 2,
            'ngpus': 1,
            'ncputhreads': 1,
            'precision':'single',
        },
    },

    'qsim-mgpu': {
        'config': {
            'nshots': 1024,
            'nfused': 4,
            'ngpus': 8,
            'ncputhreads': 1,
            'precision':'single',
        },
    },

}
