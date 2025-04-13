fpath = fullfile(pwd,'wine-quality.csv');                           %file path
%fname = readtable(fpath, 'VariableNamingRule', 'preserve');         %correct read file

% Wczytanie danych
fname = readtable(fpath, 'VariableNamingRule', 'preserve');

% Wybranie pierwszych 5 wierszy
firstFive = head(fname, 5);

% Transpozycja
verticalView = array2table(firstFive.Variables', ...
    'VariableNames', strcat("Sample", string(1:5)), ...
    'RowNames', fname.Properties.VariableNames);

% Kolory w ANSI (w terminalu)
colors = ["\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[35m", "\033[36m"];
reset = "\033[0m";

% Wyświetlanie wierszy z kolorami
disp('--- Pierwsze 5 próbek w widoku pionowym (kolor) ---');
for i = 1:height(verticalView)
    color = colors(mod(i-1, numel(colors)) + 1);  % Cykl przez kolory
    rowName = verticalView.Properties.RowNames{i};
    values = table2array(verticalView(i, :));
    fprintf([color, '%s: ', reset], rowName);
    fprintf('%g  ', values);
    fprintf('\n');
end
