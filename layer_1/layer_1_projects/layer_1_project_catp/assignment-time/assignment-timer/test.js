#!/usr/bin/env node

import chalk from 'chalk';
import figlet from 'figlet';

console.clear();
console.log(chalk.cyan(figlet.textSync('Assignment Timer', { horizontalLayout: 'full' })));
console.log(chalk.gray('Track your assignment completion times\n'));

console.log(chalk.green('✅ CLI application is working!'));
console.log(chalk.blue('📚 Features:'));
console.log(chalk.yellow('  • Start/Stop timer for assignments'));
console.log(chalk.yellow('  • Select from Canvas assignments'));
console.log(chalk.yellow('  • Save timing data to Firestore'));
console.log(chalk.yellow('  • View timing history'));
console.log(chalk.yellow('  • Beautiful CLI interface'));

console.log(chalk.cyan('\n🚀 Ready to use! Run: npm start'));
